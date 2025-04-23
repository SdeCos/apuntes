### Mirar deferencia entre PDO y MYSQL en php

# Diseño (Diagrama Xen)

## Entidad

Hace referencia a algun objeto de la vida real, como por ejemplo "instructor", "student"... , pueden ser **fuertes**, representadas por un **rectangulo con una sola linea**, mientras que la **debil**, es un **rectangulo con doble linea**.\
Al borrar un registro perteneciente a una entidad debil hay que hacerlo en cascada.

## Relacion

Representada por un **rombo**, si une dos **entidades fuertes**, se dibuja con una sola linea, mientras que si une una **fuerte** con una **debil**, hay que dibujarla con doble capa.

## Tipos de Relaciones

n, m: Mucho a mucho, cuando existe esta relacion, **se genera una tercera tabla**.
1, \*: Uno a muchos, **no** genera otra tabla.

### Ejemplo tabla generada en relacion mucho a mucho

- Relacion: Instructor - Student, unido por la relacion tutor, relacion n, m
  Esta relacion genera una tabla tutor con los siguientes datos, **id**, **idstudent**, **idinstructor**, **semestre**.

| ID  | IdStudent | IdInstructor | Semestre |
| --- | --------- | ------------ | -------- |
| 1   | 1         | 1            | Primero  |
| 2   | 1         | 2            | Primero  |

## Consultas SQL

### Para buscar informacion ausente no hay que poner el where is null
