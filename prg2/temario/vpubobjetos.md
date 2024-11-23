# Vista publica de los objetos

| Creación                        | Referencia                                      | Interacción     |
| ------------------------------- | ----------------------------------------------- | --------------- |
| Crear objetos                   | Referenciar objetos                             | Enviar mensajes |
| Creación de vectores de objetos | Referencia a un vector de referencias a objetos |                 |

## Creación de objetos

**new** es un operador cuyo operando es una clase de objetos y **devuelve la dirección de memoria donde se ha reservado el espacio para dicho objeto.**

### Sintaxis

```java
new <Clase>([<expresion>, ...])
```

- La lista de expresiones debe coincidir con los parámetros de alguno de los constructores de la clase.
- En caso de no exister constructor, la lista debe estar vacía.
  ![creacion de objetos](../imagenes/creacionDeObjetos.jpg)

## Referencia a un objeto

Variable puntero que alberga la dirección de un objeto de una clase.

```
[final] <Clase> <referencia> [=<direccion>];
```

- A falta de inicialización, su dirección es null.
- **final** obliga a la inicialización y fija su valor para la referencia.

```java
Intervalo intervalo;
```

![referencia a objeto](../imagenes/referenciaAObjeto.png)

### Operadores

|                                    |                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------- |
| `<referencia0> = <direccion0>`     | Asigna la dirección a la referencia siendo del mismo tipo              |
| `<direccionO-I> == <direccionO-D>` | Determina si dos direcciones a objetos de la misma clase son iguales   |
| `<direccionO-I> != <direccionO-D>` | Determina si dos direcciones a objetos de la misma clase son distintas |

```java
final Intervalo HORARIO = new Intervalo(7,15);
Intervalo edades = new Intervalo(100);
Intervalo anos;
anos = edades;
boolean mismo = edades == anos;
```

## Paso de mensajes

```
<expression>.<methodName>([<expression>{, <expression>}])
```

Donde el método debe estar presente en la interfaz de la clase del objeto y las expresiones deben coincidir con los parámetros del método.

```java
intervalo.longitud();
new Intervalo(-100,100).longitud();
edades.partidos(5);
anos.incluye(88);
edades.interseccion(anos);
```
