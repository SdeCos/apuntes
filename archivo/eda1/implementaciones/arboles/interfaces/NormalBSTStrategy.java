package interfaces;

class NormalBSTStrategy implements InsertionStrategy {
  @Override
  public boolean goLeft(Node current, int value) {
    return value < current.value;
  }
}
