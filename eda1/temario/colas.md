# Colas

## ¿Por qué?

- Proporcionan una manera eficiente de manejar datos con un comportamiento "primero en entrar, primero en salir" (FIFO).
- Esenciales para modelar situaciones de espera.

## ¿Qué?

Estructura de datos lineal que sigue el principio FIFO (First In, Firts Out).

- Los elementos son añadidos al final de la cola y eliminados desde el frente.
- El primer elemento insertado es el primero en salir
- Operaciones básicas:
  - **Enqueue**: añadir elemento al final de la cola
  - **Dequeue**: eliminar el elemento del frente de la cola
  - **Peek** o **Front**: ver el elemento en el frente sin eliminarlo
- Puede implementarse mediante arrays o listas enlazadas

## ¿Para qué?

- Gestión de procesos
- Manejo de solicitudes
- Búfers
- Gestión de tareas en impresoras
- etc.

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

public class Cola {
    private Nodo frente;
    private Nodo final;

    public Cola() {
        this.frente = null;
        this.final = null;
    }

    public void enqueue(int valor) {
        Nodo nuevoNodo = new Nodo(valor);
        if (estaVacia()) {
            frente = nuevoNodo;
            final = nuevoNodo;
        } else {
            final.siguiente = nuevoNodo;
            final = nuevoNodo;
        }
    }

    public int dequeue() {
        if (estaVacia()) {
            System.out.println("La cola está vacía");
            return -1;
        }
        int valor = frente.dato;
        frente = frente.siguiente;
        if (frente == null) {
            final = null;
        }
        return valor;
    }

    public int peek() {
        if (estaVacia()) {
            System.out.println("La cola está vacía");
            return -1;
        }
        return frente.dato;
    }

    public boolean estaVacia() {
        return frente == null;
    }

    public void imprimirCola() {
        Nodo actual = frente;
        System.out.print("Frente -> ");
        while (actual != null) {
            System.out.print(actual.dato + " -> ");
            actual = actual.siguiente;
        }
        System.out.println("Final");
    }
}

public class EjemploCola {
    public static void main(String[] args) {
        Cola cola = new Cola();
        cola.enqueue(1);
        cola.enqueue(2);
        cola.enqueue(3);
        cola.imprimirCola();
        System.out.println(cola.dequeue());
        System.out.println(cola.peek());
        cola.imprimirCola();
    }
}
```
