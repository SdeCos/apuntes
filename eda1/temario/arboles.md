# Arboles

## ¿Por qué?

Después de comprender estructuras de datos lineales como listas, pilas y colas, hay que avanzar hacia estructuras más complejas como los árboles.
Permiten represntar datos de una manera jerárquica, crucial para muchas aplicaciones, como:

- Sistemas de archivos
- Bases de datos
- Procesamiento de lenguaje natural
- Algoritmos de búsqueda y clasificación
- Árboles DOM en desarrollo web
- Árboles de decisión en IA
- Estructura de JSON/XML

## ¿Qué?

Un árbol es una estructura de datos **no lineal**, simula una jerarquía utilizando relaciones padre-hijo, consiste en **nodos** conectados.

### Comparación con Listas

| Lista                                                            | Árbol                                                  |
| ---------------------------------------------------------------- | ------------------------------------------------------ |
| Cada elemento tiene como máximo un elemento anterior y siguiente | Un nodo puede tener múltiples hijos (nodos siguientes) |
| Camino único para recorrer todos los elementos                   | Múltiples caminos para llegar a distintos elementos    |
| [!lista](../../imagenes/lista.svg)                               | [!arbol](../../imagenes/arbol.svg)                     |

## ¿Para qué?

- **Representar datos jerárquicos**
- **Facilitar búsquedas**
- **Manejar datos ordenados**
- **Optimizar operaciones**
- **Compilación y Parsing**
  - [Árboles de sintaxis abstracta(AST)](ast.md)
- **Inteligencia Artificial**
- **Gáficos y videojuegos**
- **Sistemas operativos**
- **Redes y comunicaciones**

## ¿Cómo?

### Implementación básica

- Cada nodo contiene datos y referencias a sus nodos hijos.
- La implementación varía según el tipo de árbol.

[!arbol caracteristicas](../../imagenes/arbolCaracteristicas.svg)

<table>
    <tr>
        <td colspan="3"> Características</td>
    </tr>
    <tr>
        <td>Nodo raíz</td>
        <td>Nodo Superior (Sin padres)</td>
        <td>'a' es el nodo raíz</td>
    </tr>
    <tr>
        <td>Nodos hijos</td>
        <td>Nodos que descienden de otros</td>
        <td>'b' y 'c' son hijos de 'a'</td>
    </tr>
    <tr>
        <td>Nodo padre</td>
        <td>Nodos que tiene hijos</td>
        <td>'a' es padre de 'b' y 'c'</td>
    </tr>
    <tr>
        <td>Hojas</td>
        <td>Nodos sin hijos</td>
        <td>'d', 'e', 'f', 'g' son hojas</td>
    </tr>
    <tr>
        <td>Nodos internos</td>
        <td>Nodos que tienen al menos un hijo</td>
        <td>'a', 'b', 'c' son internos</td>
    </tr>
    <tr>
        <td>Nivel</td>
        <td>Conjunto de nodos a la misma profundidad</td>
        <td>Nivel 0:{a}</br>Nivel 1:{b,c}</br>Nivel 2:{d,e,f,g}</td>
    </tr>
    <tr>
        <td>Altura del árbol</td>
        <td>Altura del nodo raíz</td>
        <td>La altura es 2</td>
    </tr>
    <tr>
        <td>Grado</td>
        <td>Número máximo de hijos que puede tener un nodo</td>
        <td>'a' tiene grado 2 </br> 'c' tiene grado 3</td>
    </tr>
    <tr>
        <td>Camino</td>
        <td>Secuencia de nodos conectados desde un nodo hasta otro</td>
        <td>De 'a' a 'f': a→c→f</td>
    </tr>
</table>

### Operaciones

- Inserción: Agregar nodos respetando las propiedades del árbol
- Recorrido: Visitar todos los nodos en un orden específico
- Búsqueda: Encontrar un nodo específico
- Eliminación: eliminar nodos manteniendo la estrcutura del árbol
