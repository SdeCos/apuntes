###UNION\
**select s.name from student as s where s.major='Mathematic' UNION select ps.name from instructor as ps where ps.major='Computer Science'**\
Selecciona el nombrer del estudiante que esta estudiando matematicaas y lo une al estudiante que esta estudiando computer science\
**select s.name from student as s where s.major='Mathematics' UNION select ps.name from instructor as ps where ps.major='Computer Science';**\
Se puede utilizar para seleccionar contenido de varias tablas diferentes, en este caso estoy seleccionando los estudiantes que dan matematicas y el instructor que da Computer Science\
###PRODUCTO CARTESIANO\
**select \* from student as s cross join instructor as i;**\
Multiplica ambas tablas, combinando todos los datos de la primera con todos los datos de la segunda\
###INTERSECCION\
**select s.major from student as s intersect select i.major from instructor as i;**\
###DIFERENCIA
select i.name from instructor as i where not exists (select 1 from instructor as ins where ins.instructor\*id=i.instructor_id and ins.major='Computer Science');
El 1 del segundo select aumenta la eficiencia, esta consulta selecciona todos los instructores que no tienen como major computer science, para diferencias se usa not exists, NO USAR not in\
###RENOMBRAMIENTO\
No es necesario el as para renombrar a partir de from
###NATURAL JOIN
**select \* from student natural join enrollments;**
Equivalente al inner join, si tienen una columna en comun hace el **as** del inner join automaticamente, si no tienen ninguna columna en comun hace un producto cartesiano, la unica diferencia con en inner join es que el inner join muestra columnas repetidas
###LEFT/RIGHT OUTER JOIN
**select \* from student right outer join enrollments on enrollments.student_id=student.student_id;**
Se utilizan para buscar informacion ausente
###MEDIA/COUNT
**select AVG(i.salary) as salary from instructor i group by i.name;**
Media de salario por departamento
**select count(i.name) as count from instructor i;**
Cuenta la cantidad de filas de la tabla
