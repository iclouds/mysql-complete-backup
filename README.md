# MySQL Complete Backup / Backup Completo do MySQL 

![](https://www.python.org/static/community_logos/python-powered-w-100x40.png) |
<img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/62/MySQL.svg/1200px-MySQL.svg.png" width="100" height="40" />

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
  
  # License / Licença
  
  Copyright [2019] [iClouds - Web Systems]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
