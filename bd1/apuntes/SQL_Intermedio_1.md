#SQL Intermedio I
### REPASAR
InnoDB y MyISAM diferencias
Test de comparacion o algo asi
##INSERT
inserta datos Ej: **INSERT INTO `instructor`(`ID`,`name`,`dept_name`,`salary`) VALUES ('243662','Hitman','Comp. Sci.', '20023.00');**
Ej en bd uni_2025: **INSERT INTO `student`(`ID`,`name`,`dept_name`,`tot_cred`) VALUES ('23454', 'Saul', 'Comp. Sci.', 6);**
##UPDATE
**update `student` set `tot_cred`=60 where student.id='23454';**
**update `student` set `name`='De Cos' where student.id='23454';**
Ej: Aumenta el salario de todos los instructores en un 5%
**update instructor set salary = salary * 1.05;**
###SUBCONSULTA
**update instructor set salary = salary * 1.05 where salary < (SELECT * FROM (SELECT avg(salary) FROM instructor)tempSalary);**
##DELETE
Ej: Eliminar todas las tuplas de innstructor asociados con el departamento localizado en Watson
**delete from instructor where dept_name in (select dept_name from department where building = 'Watson');**
##OPERACIONES BINARIAS SOBRE UNA RELACION
UNION INTERSECCION Y DIFERENCIA, PRODUCTO CARTESIANO
##PRODUCTO CARTESIANO
select * from student,instructor;
##UNION
SELECT section.course_id FROM `section` WHERE semester='Fall' and year = 2017 UNION SELECT section.course_id FROM `section` WHERE semester='Spring' and year=2018;
Ej mal empleado: select * from student as s union select * from instructor as i;
Une salario con creditos, habria que seleccionar datos del mismo esquema
##INTERSECCION
SELECT * FROM instructor WHERE dept_name = 'Music' INTERSECT SELECT * FROM instructor where salary > 12000.00;
#PROCEDURE
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
