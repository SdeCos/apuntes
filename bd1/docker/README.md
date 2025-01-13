# Docker

## Comandos

Para iniciar docker **sudo docker-compose up -d**\
Para conectarse **mysql -h 127.0.0.1 -p 3307 -u saul -p**\

### Imporar base de datos

Para acceder a la consola del contenedor **docker exec -it mysql_bd /bin/bash**\
Una vez en el bash del contendor, ir a la carpeta compartida **cd shared-folder**\
Ya en la carpeta, se ejecuta el comando de importar la base de datos normalmente **mysql -u saul -p nombre_bd < archivo.sql**\

## Estructura

- **docker-compose.yml**: Configuracion docker, cambia el puerto por el que se inicia al 3307, y mapea init.sql, shared y mysql_data.
- **init.sql**: Comandos que ejecuta mysql al iniciarse.
- **mysql_data**: Guarda las modificaciones para no perderlas al parar el contenedor.
- **shared**: Carpeta compartida con el contenedor para pasarle archivos .sql con bases de datos.
