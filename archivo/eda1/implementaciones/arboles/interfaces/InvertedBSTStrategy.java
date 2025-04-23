package interfaces;

class InvertedBSTStrategy implements InsertionStrategy {
  @Override
  public boolean goLeft(Node current, int value) {
    return value > current.value;
  }
}
