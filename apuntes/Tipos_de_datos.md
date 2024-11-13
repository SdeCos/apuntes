### Crear bd
create database 'nombre';
### Eliminar tabla
drop table if exists 'nombre';
### Creacion tabla student
CREATE TABLE IF NOT EXISTS `student` ( `ID` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL, `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL, `dept_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL, `tot_credit` decimal(3,0) DEFAULT NULL, PRIMARY KEY (`ID`), KEY `dept_name` (`dept_name`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
Una vez creada, si se quiere ver la estructura se usa el comando **desc 'nombre';**
Si se copia la tabla en una nueva mediante el comando **create table 'nombre2' as select * from 'nombre';** se copian los datos pero no se copian ni **key** ni **primary key**
### Collation
Tipo de dato, dependiendo de este puede que reconozca o no acentos o la n~, consume mas espacio
Hay 2 tipos de espanol, el moderno(utf8_spanish2_ci) u el tradicional (utf8_spanish+ci), el tradicional considera "ch" como una letra entre la "c" y la "d", ademas de "ll" entre la "l" y la "m".
###Tipos de datos
####Numericos
tinyint (1 byte) de -128 a 127 o, si no tiene signo (unsigned), de 0 a 255
smallint (2 bytes) de -32768 a 32767 o, si no tiene signo, de 0 a 65535 
mediumint (3 bytes) de -8388608 a 8388607 o, si no tiene signo, de 0 a 16777215
int/integer (4 bytes) de -2147483648 a 2147483647 o, si no tiene signo, de 0 a 4294967295
bigint (8 bytes) de -9223372036854775808 a 9223372036854775807 o, si no tiene signo de 0 a 18446744073709551615
####Char y Varchar
Char siempre utiliza todos los bytes asignados, mientras que varchar es dinamico, usando solo los bytes necesarios.
Ej: Una celca con valor nulo pero tipo de dato char(4) utiliza 4 bytes, mientras que si es varchar(4), solo utilizara 1
Char tiene mejor rendimiento pero pierdes espacio de almacenamiento, varchar funciona al reves, ahorras espacio pero pierdes rendimiento
####ENUM  y SET
Enum es una lista de datos se declara, por ejemplo enum('red', 'green', 'blue') son los valores disponibles para una columna de una tabla, no permite poner valores fuera de 'red', 'green' o 'blue', y, set, es como enum, pero permite elegir ninguno, uno o varios
####Fechas
date 'yyyy-mm-dd' 
time 'hh:mm:ss'
datetime combinacion de ambas 'yyyy-mm-dd hh:mm:ss'
timestamp combinacion de fecha y hora pero con menos rango de tiempo, del 1 de enero de 1970 a 2037


