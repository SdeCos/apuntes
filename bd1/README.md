# Comandos Maquina Virtual

ssh-keygen -t rsa -b 4096 -C "saul.decossanchez@alumnos.uneatlantico.es"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
git config --global user.name SdeCos
git config --global user.email saul.decossanchez@alumnos.uneatlantico.es

sudo apt update
sudo apt upgrade
sudo apt install mysql
sudo apt install git

## Crear usuario root mysql

sudo mysql -u root -p
CREATE USER 'saul'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON _._ TO 'saul'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'username'@'localhost';
