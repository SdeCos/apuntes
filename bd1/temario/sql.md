# SQL

## SIGLAS

DBMS: Database Management System
DDL: Data Definition Language
DML: Data Manipulation Language

## UNION

- Se utiliza para unir el resultado de varios SELECT

**select s.name from student as s where s.major='Mathematic' UNION select ps.name from instructor as ps where ps.major='Computer Science'**\

- Selecciona el nombre del estudiante que esta estudiando matematicaas y lo une al estudiante que esta estudiando computer science\
  **select s.name from student as s where s.major='Mathematics' UNION select ps.name from instructor as ps where ps.major='Computer Science';**\
- Se puede utilizar para seleccionar contenido de varias tablas diferentes, en este caso estoy seleccionando los estudiantes que dan matematicas y el instructor que da Computer Science\

## PRODUCTO CARTESIANO

- Combina todas las filas de dos o mas tablas

**select \* from student as s cross join instructor as i;**\

- Multiplica ambas tablas, combinando todos los datos de la primera con todos los datos de la segunda\

## INTERSECCION

- Devuelve filas comunes a dos conjuntos de resultados SELECT

**select s.major from student as s intersect select i.major from instructor as i;**\

## DIFERENCIA

- Devuelve las filas que estan en el primer SELECT pero no en el segundo

select i.name from instructor as i where not exists (select 1 from instructor as ins where ins.instructor\*id=i.instructor_id and ins.major='Computer Science');

- El 1 del segundo select aumenta la eficiencia, esta consulta selecciona todos los instructores que no tienen como major computer science, para diferencias se usa not exists, NO USAR not in\

## RENOMBRAMIENTO

- Cambia el nombre de la columna

- No es necesario el as para renombrar a partir de from

## NATURAL JOIN

- Combina automaticamente las filas de dos tablas basandose en columnas con el mismo nombre

**select \* from student natural join enrollments;**
Equivalente al inner join, si tienen una columna en comun hace el **as** del inner join automaticamente, si no tienen ninguna columna en comun hace un producto cartesiano, la unica diferencia con en inner join es que el inner join muestra columnas repetidas

## LEFT/RIGHT OUTER JOIN

### Left

- Devuelve todas las filas de la tabla izquierda y las coincidentes de la derecha

### Right

- Devuelve todas las filas de la tabla derecha y las coincidented de la izquierda

### Outer

- Devuelve todas las filas de ambas tablas, con coincidencias cuando existen

**select \* from student right outer join enrollments on enrollments.student_id=student.student_id;**

- Se utilizan para buscar informacion ausente

## MEDIA/COUNT

**select AVG(i.salary) as salary from instructor i group by i.name;**

- Media de salario por departamento

**select count(i.name) as count from instructor i;**

- Cuenta la cantidad de filas de la tabla

## SELECT DISTINCT

- Es el equivalente a la proyeccion del algebra relacional, elimina duplicados

## Seleccion

- Procedimiento de seleccion de tuplas que satisfacen un predicado, sigma en algebra relacoinal, su equivalente en mysql es WHERE

## Patrones de busqueda

### TEST DE COMPARACION

- Compara una cosa con otra (mayor, menor, igual, distinto, mayor o igual...)

### COMPOSICIONES COMPUESTAS DE COMPARACION

**AND OR NOT** Ej: select \* from `section where `course+id`=BIO-101` AND `year`=`2017`

### RANGOS

**BETWEEN** Ej: SELECT \* FROM `instructor` WHERE `salary` BETWEEN '60000' and '87000'

### TEST DE MEMBRESIA

**IN** Ej: SELECT \* FROM `section` WHERE `course_id` IN ('BIO-101', 'BIO-301')

### TEST DE COINCIDENCIA DE PATRONES

**LIKE** Ej: SELECT \* FROM `student` WHERE `dept_name` LIKE 'Comp%'

### TEST DEL VALOR NULL

**IS NULL** Ej: SELECT \* FROM `takes` WHERE `grade` IS NULL

## ORDENAMIENTO

**ORDER BY** Ej: SELECT _ FROM `section` ORDER BY `semester`, puede ordenarse por multiples a la vez ademas de poder decir si va a ser en orden descendiente (DESC) o ascendente (ASC) Ej: SELECT _ FROM section ORDER BY semester, building

## RENOMBRAMIENTO

CREATE TABLE **nombre_nuevo** SELECT DISTINCT \_ FROM **nombre_antiguo**; puede crearse con menos columnas, seleccionando unicamente las que se quieren copiar

## RENOMBRAMIENTO DE COLUMNAS

SELECT DISTINCT ID, **columna nombre antigua** AS **cloumna nombre nuevo** , dept_name AS departamento, salary AS salario FROM profesor;

## VISTA

CREATE VIEW end AS SELECT \_ FROM instructor WHERE salary<48000; Crea una vista
selet \* from end; Selecciona todo el contenido de la vista creada
Para eliminarla drop view end;

## INSERT

inserta datos Ej: **INSERT INTO `instructor`(`ID`,`name`,`dept_name`,`salary`) VALUES ('243662','Hitman','Comp. Sci.', '20023.00');**
Ej en bd uni_2025: **INSERT INTO `student`(`ID`,`name`,`dept_name`,`tot_cred`) VALUES ('23454', 'Saul', 'Comp. Sci.', 6);**

## UPDATE

**update `student` set `tot_cred`=60 where student.id='23454';**
**update `student` set `name`='De Cos' where student.id='23454';**
Ej: Aumenta el salario de todos los instructores en un 5%
**update instructor set salary = salary \* 1.05;**

### SUBCONSULTA

**update instructor set salary = salary _ 1.05 where salary < (SELECT _ FROM (SELECT avg(salary) FROM instructor)tempSalary);**

## DELETE

Ej: Eliminar todas las tuplas de innstructor asociados con el departamento localizado en Watson
**delete from instructor where dept_name in (select dept_name from department where building = 'Watson');**

## OPERACIONES BINARIAS SOBRE UNA RELACION

UNION INTERSECCION Y DIFERENCIA, PRODUCTO CARTESIANO

## PRODUCTO CARTESIANO

select \* from student,instructor;

## UNION

SELECT section.course*id FROM `section` WHERE semester='Fall' and year = 2017 UNION SELECT section.course_id FROM `section` WHERE semester='Spring' and year=2018;
Ej mal empleado: select * from student as s union select \_ from instructor as i;
Une salario con creditos, habria que seleccionar datos del mismo esquema

## INTERSECCION

SELECT _ FROM instructor WHERE dept_name = 'Music' INTERSECT SELECT _ FROM instructor where salary > 12000.00;

## PROCEDURE

DELIMITER $$
CREATE DEFINER = `root`@`localhost` PROCEDURE `bd_espacio_en_memoria`()
NO SQL
BEGIN

END$$
DELIMITER;

En terminal con consulta:
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE 
`test_comparison`()
BEGIN
select * from instructor;
END $$
DELIMITER;

Para ejecutarlo
CALL test_comparison();

# Creacion de tablas

## Crear bd

create database 'nombre';

## Eliminar tabla

drop table if exists 'nombre';

## Creacion tabla student

CREATE TABLE IF NOT EXISTS `student` ( `ID` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL, `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL, `dept_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL, `tot_credit` decimal(3,0) DEFAULT NULL, PRIMARY KEY (`ID`), KEY `dept_name` (`dept_name`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
Una vez creada, si se quiere ver la estructura se usa el comando **desc 'nombre';**
Si se copia la tabla en una nueva mediante el comando **create table 'nombre2' as select \* from 'nombre';** se copian los datos pero no se copian ni **key** ni **primary key**

## Collation

Tipo de dato, dependiendo de este puede que reconozca o no acentos o la n~, consume mas espacio
Hay 2 tipos de espanol, el moderno(utf8_spanish2_ci) u el tradicional (utf8_spanish+ci), el tradicional considera "ch" como una letra entre la "c" y la "d", ademas de "ll" entre la "l" y la "m".

## Tipos de datos

### Numericos

tinyint (1 byte) de -128 a 127 o, si no tiene signo (unsigned), de 0 a 255
smallint (2 bytes) de -32768 a 32767 o, si no tiene signo, de 0 a 65535
mediumint (3 bytes) de -8388608 a 8388607 o, si no tiene signo, de 0 a 16777215
int/integer (4 bytes) de -2147483648 a 2147483647 o, si no tiene signo, de 0 a 4294967295
bigint (8 bytes) de -9223372036854775808 a 9223372036854775807 o, si no tiene signo de 0 a 18446744073709551615

### Char y Varchar

Char siempre utiliza todos los bytes asignados, mientras que varchar es dinamico, usando solo los bytes necesarios.
Ej: Una celca con valor nulo pero tipo de dato char(4) utiliza 4 bytes, mientras que si es varchar(4), solo utilizara 1
Char tiene mejor rendimiento pero pierdes espacio de almacenamiento, varchar funciona al reves, ahorras espacio pero pierdes rendimiento

### ENUM y SET

Enum es una lista de datos se declara, por ejemplo enum('red', 'green', 'blue') son los valores disponibles para una columna de una tabla, no permite poner valores fuera de 'red', 'green' o 'blue', y, set, es como enum, pero permite elegir ninguno, uno o varios

### Fechas

date 'yyyy-mm-dd'
time 'hh:mm:ss'
datetime combinacion de ambas 'yyyy-mm-dd hh:mm:ss'
timestamp combinacion de fecha y hora pero con menos rango de tiempo, del 1 de enero de 1970 a 2037

### Tipos de datos numericos de punto flotante

DROP TABLE IF EXISTS `flotantes`; CREATE TABLE IF NOT EXISTS `flotantes` (`id` int NOT NULL AUTO_INCREMENT, `float` float NOT NULL, `double` double NOT NULL, `real` double NOT NULL, `decimal_d_mayor_cero` decimal(10,2) NOT NULL, `decimal_d_igual_cero` decimal(10,0) NOT NULL, PRIMARY KEY(`id`) ) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
AUTO_INCREMENT = 3, hace que el auto increment empieze en 3

## Test

INSERT INTO flotantes(`id`, `float`, `double`, `real`, `decimal_d_mayor_cero`, `decimal_d_igual_cero`) VALUES(3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793)
id = 3, float = 3.14159, double = 3.141592653589793, decimal_d_mayor_cero = 3.14, decimal_d_igual_cero = 3

## Tipos de datos 2

DROP TABLE IF EXISTS `decimal_table`; CREATE TABLE IF NOT EXISTS `decimal_table`(`id` int NOT NULL AUTO_INCREMENT, `field_2,1` decimal(2,1) DEFAULT NULL, `field_8,2` decimal(8,2) DEFAULT NULL, `field_10,2` decimal(10,2) DEFAULT NULL, `field_10,4` decimal(10,4) DEFAULT NULL, PRIMARY KEY(`id`) ) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

## Test 2

INSERT INTO decimal_table(`id`, `field_2,1`, `field_8,2`, `field_10,2`, `field_10,4`) VALUES(3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793);
id = 3, field_2,1 = 3.1, field_8,2 = 3.14, field_10,2 = 3.14, field_10,4 = 3,1416

## Collate y Charset

DROP TABLE IF EXISTS `collation_case`; CREATE TABLE IF NOT EXISTS `collation_case` (`id` int NOT NULL AUTO_INCREMENT, `utf8_unicode_ci` char(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL, `latin1_general_cs` char(10) CHARACTER SET latin1 COLLATE latin1_general_cs DEFAULT NULL, `ascii_general_ci` char(10) CHARACTER SET ascii COLLATE ascii_general_ci DEFAULT NULL, `utf8_bin` char(10) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL, `latin1_bin` char(10) CHARACTER SET latin1 COLLATE latin1_bin DEFAULT NULL, `ascii_bin` char(10) CHARACTER SET ascii COLLATE ascii_bin DEFAULT NULL, PRIMARY
