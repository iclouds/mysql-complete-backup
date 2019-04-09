#!/usr/bin/python 
import os
import commands
import pipes
import mysql.connector
from settings import *

os.system("find "+ BACKUP_PATH +" -type f -mtime "+ TIME +" -delete")

#<begin>
#Conexao com o banco de dados
conn = mysql.connector.connect (
  user = DB_USER,
  password = DB_USER_PASSWORD,
  host = DB_HOST,
  buffered = True
)

cursor = conn.cursor()
databases = ("show databases")
cursor.execute(databases)
# #<end>

# #<begin> 
# - Escreve no arquivo de texto DB_NAME o array de nomes de bases de dados com quebra de linha.
outF = open(DB_NAME, "w")

for (databases) in cursor:
  dbs = databases[0] + "\n"
  outF.writelines(dbs)
outF.close()
#<end>

#<begin> 
# - Cria a pasta de backup a data e hora de hoje se nao existir
# - Verifica se o DB_NAME e um nome de base ou uma lista de texto de nomes de db.
# - Verifica quantidade de linhas e realiza o dump de cada base de dados.
# - Ele sera armazenado em TODAYBACKUPPATH.

try:
  os.stat(TODAYBACKUPPATH)
except:
  os.mkdir(TODAYBACKUPPATH)

print ("checking for databases names file.")
if os.path.exists(DB_NAME):
  file1 = open(DB_NAME)
  multi = 1
  print ("Databases file found...")
  print ("Starting backup of all dbs listed in file " + DB_NAME)
else:
  print ("Databases file not found...")
  print ("Starting backup of database " + DB_NAME)
  multi = 0

if multi:
  in_file = open(DB_NAME,"r")
  flength = len(in_file.readlines())
  in_file.close()
  p = 1
  dbfile = open(DB_NAME,"r")

  while p <= flength:
    db = dbfile.readline()   # reading database name from file
    db = db[:-1] # deletes extra line

    dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " --databases " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
      
    os.system(dumpcmd)
    gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
    os.system(gzipcmd)
    p = p + 1
  dbfile.close()
else:
  db = DB_NAME
  dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " --databases " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
  os.system(dumpcmd)
  gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
  os.system(gzipcmd)

print ("Backup script completed")
print ("Your backups have been created in '" + TODAYBACKUPPATH + "' directory")
#<end>

try:
  os.system(
    "cd " + BACKUP_PATH + 
    " && tar -czvf " + 
    BACKUP_PATH+"/"+CUSTOMER+"_"+DATETIME+".tar.gz " + 
    DATETIME
  )
except:
  print("Ocorreu um erro ao tentar compactar a pasta de backup "+ DATETIME)

try:
  os.system(
    "cd " + BACKUP_PATH + 
    " && rm -R " + DATETIME
  )
except:
  print("Ocorreu um erro ao tentar excluir a pasta de backup "+ DATETIME)

try:
  os.system(
    "scp " + 
    BACKUP_PATH + "/" + 
    CUSTOMER+"_"+DATETIME+".tar.gz " + 
    REMOTE_BACKUP_USER+"@"+REMOTE_BACKUP_HOST+":"+REMOTE_BACKUP_DIR
  )
except:
  print("Occoreu um erro na transferencia de backup para o servidor.")

try:
  os.system(
    "ssh " + 
    REMOTE_BACKUP_USER+"@"+REMOTE_BACKUP_HOST +
    " find " + REMOTE_BACKUP_DIR +
    " -type f -mtime "+ TIME + 
    " -delete && exit"
  )
except:
  print("Occoreu um erro na conexao ssh.")

try:
  os.system("rm " + DB_NAME + " && " + "rm settings.pyc")
except:
  print("Occoreu um erro na conexao ssh.")