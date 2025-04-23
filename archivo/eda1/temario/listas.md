# Listas

## ¿Por qué?

- Ofrecen una alternativa flexible a los arrays, permitiendo una getión dinámica de la memoria
- Esenciales para desarrollar habilidades avanzadas en programación

## ¿Qué?

Estructura de datos **lineal** que consiste en una secuencia de **nodos**.

- Características principales:
  - Datos (valor almacenado).
  - Puntero o referencia al siguiente nodo.
- El último nodo apunta a null.
- No requiere un tamaño fijo predefinido.
- Tipos comunes:
  - Lista simplemente enlazada
  - Lista doblemente enlazada
  - Lista circular

## ¿Cómo?

```java
class Nodo {
    int dato;
    Nodo siguiente;

    public Nodo(int dato) {
        this.dato = dato;
        this.siguiente = null;
    }
}

class ListaEnlazada {
    private Nodo cabeza;

    public ListaEnlazada() {
        this.cabeza = null;
    }

    public void insertarAlPrincipio(int dato) {
        Nodo nuevoNodo = new Nodo(dato);
        nuevoNodo.siguiente = cabeza;
        cabeza = nuevoNodo;
    }

    public void eliminarAlPrincipio() {
        if (cabeza != null) {
            cabeza = cabeza.siguiente;
        }
    }

    public void imprimirLista() {
        Nodo actual = cabeza;
        while (actual != null) {
            System.out.print(actual.dato + " -> ");
            actual = actual.siguiente;
        }
        System.out.println("null");
    }
}

public class EjemploListaEnlazada {
    public static void main(String[] args) {
        ListaEnlazada lista = new ListaEnlazada();
        lista.insertarAlPrincipio(3);
        lista.insertarAlPrincipio(2);
        lista.insertarAlPrincipio(1);
        lista.imprimirLista();
    }
}
```

### Operaciones comnues

- Inserción al principio/final.
- Eliminación al principio/final.
- Búsqueda.
