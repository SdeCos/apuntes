public class Pila {
  private int maxTamaño;
  private int[] arregloPila;
  private int tope;

  public Pila(int tamaño) {
    maxTamaño = tamaño;
    arregloPila = new int[maxTamaño];
    tope = -1;
  }

  public void push(int valor) {
    if (tope < maxTamaño - 1) {
      arregloPila[++tope] = valor;
    } else {
      System.out.println("La pila está llena");
    }
  }

  public int pop() {
    if (!estaVacia()) {
      return arregloPila[tope--];
    } else {
      System.out.println("La pila está vacía");
      return -1;
    }
  }

  public int peek() {
    if (!estaVacia()) {
      return arregloPila[tope];
    } else {
      System.out.println("La pila está vacía");
      return -1;
    }
  }

  public boolean estaVacia() {
    return (tope == -1);
  }

  public boolean estaLlena() {
    return (tope == maxTamaño - 1);
  }
}
