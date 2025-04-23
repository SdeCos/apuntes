public class Cola {
  private Nodo frente;

  private Nodo ultimo;

  public Cola() {
    this.frente = null;
    this.ultimo = null;
  }

  public void enqueue(int valor) {
    Nodo nuevoNodo = new Nodo(valor);
    if (estaVacia()) {
      frente = nuevoNodo;
      ultimo = nuevoNodo;
    } else {
      ultimo.siguiente = nuevoNodo;
      ultimo = nuevoNodo;
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
      ultimo = null;
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
