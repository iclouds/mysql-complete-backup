# MySQL Complete Backup / Backup Completo do MySQL 

![](https://www.python.org/static/community_logos/python-powered-w-100x40.png)

This project is an python application for full backup of databases individually, it is running on scp for transfer compact files od dbs, it is configure with ".env" file :)

## Features:
  - Full Backup of databases
  - Configure with ".env" file.
  - Send backup for remote server.
  - Config default of lifetime is 7 days.

É um script em python para backup de todas as bases de dados individualmente e com envio por scp e controle ssh, configurado por um arquivo ".env".

## Features:
  - Backup Completo
  - Com configuração em um arquivo .env
  - Envio de backup para servidor remoto
  - Configuração de tempo de vida de backup (padrão  é 7 dias)



## Dependencies / Dependências
  
  - apt-get install python-pip (debian distros)
  - pip install mysql-connector-python
  - pip install environs
