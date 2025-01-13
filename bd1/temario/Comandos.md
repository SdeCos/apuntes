# Git

- Crear clave ssh: **ssh-keygen -t rsa -b 4096 -C "saul.decossanchez@alumnos.uneatlantico.es"**
- Iniciar agente ssh: **eval "$(ssh-agent -s)"**
- Añade clave ssh: **ssh-add ~/.ssh/id_rsa**
- Lee clave para copiar a git: **cat ~/.ssh/id_rsa.pub**
- Configurar nombre: **git config --global user.name SdeCos**
- Configurar email: **git config --global user.email saul.decossanchez@alumnos.uneatlantico.es**

# Docker

- Iniciar docker: **sudo docker-compose up -d**
- Concectarse a mysql como saul: **mysql -h 127.0.0.1 -p 3307 -u saul -p**
- Iniciar consola en el contenedor: **docker exec -it mysql_bd /bin/bash**
- Ir a la carpeta compartida, donde esta el archivo .sql de la base de datos: **cd shared-folder**
- Importar base de datos (antes hay que crearla): **mysql -u saul -p nombre_bd < archivo.sql**
