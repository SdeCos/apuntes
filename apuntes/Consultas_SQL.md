###UNION
**select s.name from student as s where s.major='Mathematic' UNION select ps.name from instructor as ps where ps.major='Computer Science'**\
Selecciona el nombrer del estudiante que esta estudiando matematicaas y lo une al estudiante que esta estudiando computer science\
**select s.name from student as s where s.major='Mathematics' UNION select ps.name from instructor as ps where ps.major='Computer Science';**\
Se puede utilizar para seleccionar contenido de varias tablas diferentes, en este caso estoy seleccionando los estudiantes que dan matematicas y el instructor que da Computer Science\
###PRODUCTO CARTESIANO
**select * from student as s cross join instructor as i;**\
Multiplica ambas tablas, combinando todos los datos de la primera con todos los datos de la segunda\
###INTERSECCION
**select s.major from student as s intersect select i.major from instructor as i;**
###DIFERENCIA
select i.name from instructor as i where not exists (select 1 from instructor as ins where ins.instructor_id=i.instructor_id and ins.major='Computer Science');
El 1 del segundo select aumenta la eficiencia, esta consulta selecciona todos los instructores que no tienen como major computer science\
*RENOMBRAMIENTO*
No es necesario el as para renombrar a partir de from
