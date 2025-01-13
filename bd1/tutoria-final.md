# Claves calificacion

## Comprobar que permite importar el archivo

Si no deja importar el archivo 0

## Crear procedure con las consultas

### Formato

```mysql
Begin
-- Enunciado de la preegunta
/*consulta;*/
```

## Repaso Teoria

- Esquema: orden de columnas y filas (id, nombre, apellidos) es un esquema, pero si se le añade un campo de dedad pasa a ser otro.
- Interseccion (intersect), 1 esquema, si se quiere hacer con varias tablas se pueden seleccionar los campos necesarios para que los esquemas coincidan.

  - Registros (ejemplo id nombre apellidos): tiene que haber las tuplas necesarias para que haya algun dato coincidente
    | id | n | a|
    |-|-|-|
    |1|0|3|
    |2|5|7|
    |8|6|3|
    El apellido coincide en los datos con id 1 y 8

- Diferencia, 1 esquema
- Producto cartesiano, 1 esquema con renombramiento o varios sin el.
- Reunion natural (natural join), 2 esquemas, NO hay que poner WHERE, para poder hacerla, una de las tablas ha de tener una relacion mucho a muchos, se da entre 2 esquemas con un atributo en comun
- Left/Right outer join, es necesario que haya informacion ausente (null), no llevan where
