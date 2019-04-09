import os
import time
import datetime
from environs import Env
from marshmallow.validate import Length, Email

env = Env()
env.read_env()

#*********************************************************************#
CUSTOMER = env.str("CUSTOMER", validate=[Length(min=3)])
DB_HOST = env.str("DB_HOST", validate=[Length(min=6)])
DB_USER = env.str("DB_USER", validate=[Length(min=4)])
DB_USER_PASSWORD = env.str("DB_USER_PASSWORD", validate=[Length(min=6)])
DB_NAME = env.str("DB_NAME", validate=[Length(min=2)])
BACKUP_PATH = env.str("BACKUP_PATH", validate=[Length(min=4)])

REMOTE_BACKUP_HOST= env.str("REMOTE_BACKUP_HOST", validate=[Length(min=6)])
REMOTE_BACKUP_USER = env.str("REMOTE_BACKUP_USER", validate=[Length(min=3)])
REMOTE_BACKUP_DIR = env.str("REMOTE_BACKUP_DIR", validate=[Length(min=6)])


#---------------------------------------------------------------------#
TIME= os.getenv("TIME") # Tempo limite de vida em dias de cada arquivo de backup
DATETIME = time.strftime('%Y%m%d%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME
#*********************************************************************#
