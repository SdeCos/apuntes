sudo docker-compose up -d
sleep 5
mysql -h localhost -P 3307 --protocol=tcp -u saul -p
