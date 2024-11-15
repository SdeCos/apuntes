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
###Tipos de datos numericos de punto flotante
DROP TABLE IF EXISTS `flotantes`; CREATE TABLE IF NOT EXISTS `flotantes` (`id` int NOT NULL AUTO_INCREMENT, `float` float NOT NULL, `double` double NOT NULL, `real` double NOT NULL, `decimal_d_mayor_cero` decimal(10,2) NOT NULL, `decimal_d_igual_cero` decimal(10,0) NOT NULL, PRIMARY KEY(`id`) ) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
AUTO_INCREMENT = 3, hace que el auto increment empieze en 3
###Test
INSERT INTO flotantes(`id`, `float`, `double`, `real`, `decimal_d_mayor_cero`, `decimal_d_igual_cero`) VALUES(3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793)
id = 3, float = 3.14159, double = 3.141592653589793, decimal_d_mayor_cero = 3.14, decimal_d_igual_cero = 3
###Tipos de datos 2
DROP TABLE IF EXISTS `decimal_table`; CREATE TABLE IF NOT EXISTS `decimal_table`(`id` int NOT NULL AUTO_INCREMENT, `field_2,1` decimal(2,1) DEFAULT NULL, `field_8,2` decimal(8,2) DEFAULT NULL, `field_10,2` decimal(10,2) DEFAULT NULL, `field_10,4` decimal(10,4) DEFAULT NULL, PRIMARY KEY(`id`) ) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
###Test 2
INSERT INTO decimal_table(`id`, `field_2,1`, `field_8,2`, `field_10,2`, `field_10,4`) VALUES(3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793);
id = 3, field_2,1 = 3.1, field_8,2 = 3.14, field_10,2 = 3.14, field_10,4 = 3,1416
###Collate y Charset
DROP TABLE IF EXISTS `collation_case`; CREATE TABLE IF NOT EXISTS `collation_case` (`id` int NOT NULL AUTO_INCREMENT, `utf8_unicode_ci` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL, `latin1_general_cs` char(10) CHARACTER SET latin1 COLLATE latin1_general_cs DEFAULT NULL, `ascii_general_ci` char(10) CHARACTER SET ascii COLLATE ascii_general_ci DEFAULT NULL, `utf8_bin` char(10) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL, `latin1_bin` char(10) CHARACTER SET latin1 COLLATE latin1_bin DEFAULT NULL, `ascii_bin` char(10) CHARACTER SET ascii COLLATE ascii_bin DEFAULT NULL, PRIMARY
KEY (`id`) ) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
El cs significa case sensitive, si no se quiere que sea case sensitive se usa ci, que convierte todas las mayusculas en minusculas
###Ordenamiento
DROP TABLE IF EXISTS `los_spanish`; CREATE TABLE IF NOT EXISTS `los_spanish` (`utf8_spanish_ci` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL, `utf8_spanish2_ci` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish2_ci DEFAULT NULL) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

