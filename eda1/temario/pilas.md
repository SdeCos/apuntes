# Pilas

## ¿Por qué?

- Proporcionan una forma eficiente de manejar datos con un comportamiento "último en entrar, primero en salir" (LIFOJ).
- Esenciales para entender y resolver problemas que implican recursión.

## ¿Qué?

- Los elementos se añaden y es eliminan solo desde un extremo, llamado tope de la pila.
- El último elemento insertado es el primero en ser eliminado.
- Operaciones:
  - **Push**: añade un elemento al tope de la pila
  - **Pop**: elimina el elemento del tope de la pila
  - **Peek** o **Top**: ver el elemento del tope de la pila sin eliminarlo

## ¿Para qué?

- Gestión de llamadas a funciones en la ejecución de programas
- Evaluación de expresiones matemáticas (notación polaca inversa)
- Comprobación de paréntesis y llaves en expresiones
- Implementación de la función "deshacer" en aplicaciones
- Navegación en el historial de un navegador web
- Algoritmos de recorrido en profundidad (DFS) en grafos
- Conversión de expresiones infix a postfix

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

public class Pila {
    private Nodo tope;

    public Pila() {
        this.tope = null;
    }

    public void push(int valor) {
        Nodo nuevoNodo = new Nodo(valor);
        nuevoNodo.siguiente = tope;
        tope = nuevoNodo;
    }

    public int pop() {
        if (estaVacia()) {
            System.out.println("La pila está vacía");
            return -1;
        }
        int valor = tope.dato;
        tope = tope.siguiente;
        return valor;
    }

    public int peek() {
        if (estaVacia()) {
            System.out.println("La pila está vacía");
            return -1;
        }
        return tope.dato;
    }

    public boolean estaVacia() {
        return tope == null;
    }

    public void imprimirPila() {
        Nodo actual = tope;
        System.out.print("Tope -> ");
        while (actual != null) {
            System.out.print(actual.dato + " -> ");
            actual = actual.siguiente;
        }
        System.out.println("null");
    }
}
```
