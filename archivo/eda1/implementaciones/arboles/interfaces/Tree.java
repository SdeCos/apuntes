package interfaces;

class Tree {
  private Node root;
  private InsertionStrategy strategy;

  public Tree(InsertionStrategy strategy) {
    this.root = null;
    this.strategy = strategy;
  }

  public Node getRoot() {
    return root;
  }

  public void insert(int value) {
    root = recursiveInsert(root, value);
  }

  private Node recursiveInsert(Node node, int value) {
    if (node == null) {
      return new Node(value);
    }

    if (strategy.goLeft(node, value)) {
      node.left = recursiveInsert(node.left, value);
    } else {
      node.right = recursiveInsert(node.right, value);
    }

    return node;
  }

  public void printInorder(Node node) {
    if (node == null) {
      return;
    }

    printInorder(node.left);
    System.out.print(node.value + " ");
    printInorder(node.right);
  }

  public void printPostorder(Node node) {
    if (node == null) {
      return;
    }

    printPostorder(node.left);
    printPostorder(node.right);
    System.out.print(node.value + " ");
  }

  public void printPreorder(Node node) {
    if (node == null) {
      return;
    }

    System.out.print(node.value + " ");
    printPreorder(node.left);
    printPreorder(node.right);
  }

}
