import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

  public static void main(String[] args) {

    Deque<Integer> d = new ArrayDeque<>();
    d.addFirst(1);
    d.addLast(2);
    int f = d.removeFirst();
    int l = d.removeLast();
    System.out.println("First: " + f + ", Last: " + l);
  }
}
