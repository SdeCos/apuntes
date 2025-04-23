# Vista publica de las clases

## Sintaxis

```java
class <NombreClase>{

}
```

## Cabecera de métodos de clase

```java
public <tipo1> <nombreMetodo> ({<tipo2> <parametro>, ...}*)
```

- Tipo1: Valor devuelto, si no devuelve ningun valor, se pone void
- El nombre del metodo se comienza en minúscula
- El tipo2 puede ser igual que tipo1 excepto void
- Todos los parametros son pasados por valor
  > En Java cuando se pas un parámetro a un método, lo que realmente se pasa es **una copia del valor** de ese parámetro, lo que significa que si es modificado dentro de método, no se verá reflejado fuera de este.
  > Por otra parte, cuando se trata de objetos. En Java, las variables que contienen un objeto, en realidad contienen **referencias a este**, por lo que el método puede modificar el objeto al que apunta la referencia.

## Sobrecarga de métodos

Varios métodos pueden tener el mismo nombre con restricciones:

- Si esán en la misma clase, deben diferenciarse en los parámetros que permite.
- Si están en clases distintas no hay restricción.

## Constructore

Son métodos que reúnen las tareas de inicialización (no construcción) y se lanzan automáticamente en la construcción de objetos.

- > public NombreDeLaClase()
- Deben coincidir en nombre con el de la clase.
- No devuelven nada (ni void).
- No se pueden lanzar mensajes que se correspondan con los constructores de la clase.
