(Ultimo tema parcial)
###Siglas
DBMS: Database Management System
DDL: Data Definition Language
DML: Data Manipulation Language

###SELECT DISTINCT 
Es el equivalente a la proyeccion del algebra relacional, elimina duplicados

###Seleccion
Procedimiento de seleccion de tuplas que satisfacen un predicado, sigma en algebra relacoinal, su equivalente en mysql es WHERE

##Patrones de busqueda
###TEST DE COMPARACION
Compara una cosa con otra (mayor, menor, igual, distinto, mayor o igual...)
###COMPOSICIONES COMPUESTAS DE COMPARACION
**AND OR NOT** Ej: select * from `section where `course+id`=BIO-101` AND `year`=`2017`
###RANGOS
**BETWEEN** Ej: SELECT * FROM `instructor` WHERE `salary` BETWEEN '60000' and '87000'
###TEST DE MEMBRESIA
**IN**  Ej: SELECT * FROM `section` WHERE `course_id` IN ('BIO-101', 'BIO-301') 
###TEST DE COINCIDENCIA DE PATRONES
**LIKE** Ej: SELECT * FROM `student` WHERE `dept_name` LIKE 'Comp%'
###TEST DEL VALOR NULL
**IS NULL** Ej: SELECT * FROM `takes` WHERE `grade` IS NULL
###ORDENAMIENTO
**ORDER BY** Ej: SELECT * FROM `section` ORDER BY `semester`, puede ordenarse por multiples a la vez ademas de poder decir si va a ser en orden descendiente (DESC) o ascendente (ASC) Ej: SELECT * FROM section ORDER BY semester, building
##
###RENOMBRAMIENTO
CREATE TABLE **nombre_nuevo** SELECT DISTINCT * FROM **nombre_antiguo**; puede crearse con menos columnas, seleccionando unicamente las que se quieren copiar
###RENOMBRAMIENTO DE COLUMNAS
SELECT DISTINCT ID, **columna nombre antigua** AS **cloumna nombre nuevo** , dept_name AS departamento, salary AS salario FROM profesor; 
###VISTA
CREATE VIEW end AS SELECT * FROM instructor WHERE salary<48000; Crea una vista
selet * from end; Selecciona todo el contenido de la vista creada
Para eliminarla drop view end;

