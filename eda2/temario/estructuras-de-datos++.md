# Estructuras de Datos

## [ ArrayList ](../implementaciones/estructuras-de-datos/arrayList)

Matriz redimensionable que permite almacenar elementos de cualquier tipo (incluso objetos)

### Creación

```java
ArrayList<String> myList = new ArrayList<>();
```

### Añadir elementos

```java
myList.add("Elemento 1");
myList.add("Elemento 2");
```

### Acceder a elementos

Accede al primer elemento

```java
String element = myList.get(0);
```

### Modificar elementos

Modifica el primer elemento

```java
myList.set(0, "Nuevo Elemento");
```

### Eliminar elementos

Por objeto y por índice

```java
myList.remove("Elemento 1");
myList.remove(0);
```

### Tamaño de la lista

```java
int size = myList.size();
```

### Iterar sobre elementos

```java
for (String item : myList) {
    System.out.println(item);
}
```

## [ LinkedList ](../implementaciones/estructuras-de-datos/linkedList)

Lista doblemente enlazada

### Creación

```java
LinkedList<String> list = new LinkedList<>();
```

### Añadir elementos

```java
list.add("Elemento 1");
list.addFirst("Elemento al inicio");
list.addLast("Elemento al final");
```

### Acceder a elementos

```java
String primerElemento = list.getFirst();
String ultimoElemento = list.getLast();
```

### Modificar elementos

No hay un método directo para reemplazar un elemento en una posición específica sin usar el método set(int index, E element), similar al ArrayList.

```java
list.set(1, "Nuevo Elemento");
```

### Eliminar elementos

```java
list.removeFirst();
list.removeLast();
list.remove("Elemento");
```

> El último ejemplo elimina **la primera ocurrencia** de "Elemento"

### Tamaño de la lista

```java
int size = list.size();
```

### Iterar sobre elementos

```java
for (String item : list) {
    System.out.println(item);
}
```

## [ Vector ](../implementaciones/estructuras-de-datos/vector)

Similar a una ArrayList, con mejoras de seguridad en entornos multihilo

### Creación

```java
Vector<String> vector = new Vector<>();
```

### Añadir elementos

```java
vector.add("Elemento 1");
vector.addElement("Elemento 2");
```

### Acceder a elementos

```java
String elemento = vector.get(0);
```

### Modificar elementos

```java
vector.set(0, "Nuevo Elemento");
```

### Eliminar elementos

```java
vector.remove("Elemento 1");
vector.remove(0);
```

### Tamaño del vector

```java
int size = vector.size();
```

### Iterar sobre elementos

```java
for (String item : vector) {
    System.out.println(item);
}
```

## [ Stack ](../implementaciones/estructuras-de-datos/stack)

Pila (LIFO)

### Creación

```java
Stack<String> stack = new Stack<>();
```

### Empujar (agregar) elementos

```java
stack.push("Elemento 1");
stack.push("Elemento 2");
```

### Mirar el elemento superior (sin sacarlo)

```java
String topElement = stack.peek();
```

### Sacar elementos

```java
String poppedElement = stack.pop();
```

### Comprobar si la pila está vacía

```java
boolean isEmpty = stack.isEmpty();
```

### Buscar elementos

```java
int position = stack.search("Elemento 1");
```

## [ ArrayDeque ](../implementaciones/estructuras-de-datos/arrayDeque)

Permite elementos anadidos o eliminados desde cualquiera de los dos extremos de la coleccion, es decir, funciona tanto como pila como cola

### Creación

```java
ArrayDeque<String> deque = new ArrayDeque<>();
```

### Añadir elementos

```java
deque.addFirst("Elemento al inicio");
deque.addLast("Elemento al final");
```

### Eliminar elementos

```java
deque.removeFirst();
deque.removeLast();
```

### Acceder a elementos

```java
String firstElement = deque.peekFirst();
String lastElement = deque.peekLast();
```

### Uso como pila

```java
deque.push("Nuevo Elemento");
String poppedElement = deque.pop();
```

> Primero se agrega un elemento al inicio de la pila, luego se quita y se retorna.

### Comprobar si está vacío

```java
boolean isEmpty = deque.isEmpty();
```

## [ PriorityQueue ](../implementaciones/estructuras-de-datos/priorityQueue)

Cola (FIFO)

### Creación

```java
PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
```

### Añadir elementos

```java
priorityQueue.add(10);
priorityQueue.offer(5);
```

### Acceder al elemento de mayor prioridad

```java
Integer highestPriority = priorityQueue.peek();
```

### Sacar el elemento de mayor prioridad

```java
Integer removedElement = priorityQueue.poll();
```

### Tamaño de la cola

```java
int size = priorityQueue.size();
```

### Iterar sobre elementos

Es importante notar que el iterador no garantiza recorrer los elementos en el orden de prioridad.

```java
for (Integer item : priorityQueue) {
    System.out.println(item);
}
```

## [ EnumSet ](../implementaciones/estructuras-de-datos/enumSet)

Permite crear conjuntos de elementos de un tipo de enumeracion especificado

### Creación

```java
EnumSet<DayOfWeek> days = EnumSet.noneOf(DayOfWeek.class);
```

### Añadir elementos

```java
days.add(DayOfWeek.MONDAY);
days.addAll(EnumSet.of(DayOfWeek.TUESDAY, DayOfWeek.WEDNESDAY));
```

### Eliminar elementos

```java
days.remove(DayOfWeek.MONDAY);
days.removeAll(EnumSet.of(DayOfWeek.TUESDAY, DayOfWeek.WEDNESDAY));
```

### Acceso y consulta

```java
boolean contains = days.contains(DayOfWeek.MONDAY);
boolean isEmpty = days.isEmpty();
```

### Iterar sobre elementos

```java
for (DayOfWeek day : days) {
    System.out.println(day);
}
```
