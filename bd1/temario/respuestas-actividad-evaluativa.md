# Actividad evaluativa

## Plantea una operacion UNION

Ambas tablas tienen que tener el mismo esquema, hay que seleccionar columnas identicas en 2 tablas distintas.\
Con las tablas del examen, **Instructor y Student** ambas tienen la columna **'name' y 'major'**, por lo que se seleccionan esas columnas mediante una proyeccion.\
**response_1='∏student.name,instructor.name,student.major,instructor.major(StudentsUInstructor)**

## Plantee un PRODUCTO CARTESIANO que obtenga todas las posibilidades de combinacion entre estudiantes, profesores y la especialidad

**response_2='∏students.name,students.major,instructor.name(StudentsxInstructor)'**

## Plantee una INTERSECCION sin considerar la relacion enrollment

Para hacer una interseccion, tene que haber un valor que pertenezca a ambas tablas.\
En el caso del examen, etre instructor y student, coincide **"Computer Science"** en **'Major'**. Por ello, tambien hay que proyectar la columna major unicamente.\
**response_3='∏students.major,instructor.major(Students∩Instructor)'**

## Plantee una DIFERENCIA

Ambas tablas tienen que tener el mismo esquema, y, tiene que haber algun dato que este en una pero no en la otra.\
**response_4='∏students.major(Students-Instructor)'**

## Plantee una REUNION NATURAL considerando dos relaciones

No es necesario hacer ninguna seleccion ya que solo hay una columna comun, por lo que no es necesario especificar.
**response_5='(Students⋈Enrollments)'**

## Halle valores que faltan en el proceso de los estudiantes para apuntarse en cursos

Simbolo de Reunion Externa por la izquierda
**response_6='(Students⟕Enrollments)'**

## Helle valores que falten en el proceso de matricula (enrollment) de algunos estudiantes

Simbolo de Reunion Externa por la derecha
**response_7='(Students⟖Enrollments)'**

## Obtenga los datos de los instructores que perciban mas de 6000 euros en el departamento

**response*8='σ_instructor.salary>6000^instructor.departmentid=1*(Instructor)'**

## Incremente 10 veces el salario de los instructores que ganen menos de 500 euros

**response_9='Πinstructor.salary\*10 σ_instructor.salary<500'**

## Halle el promedio del salario de todos los instructores y agrupelos por departamento

**response*10='instructor.departmentoid*Ģ*avg(instructor.salary)*(instructor)'**

## Agregue un registro y solo un registro en una de las tablas para que exista un estudiante que haya matriculado (enrollment) en todas las asignaturas.

**response_11='Πstudents.studentsid,students.name,enrollments.studentid,enrollments.course_id(Students⟖Enrollments)'**\
**response_12='Πcourse.courseid(Course)'**\
**response_13='Πstudents.name(R1:R2)'**\
**response_14='Alice'**
