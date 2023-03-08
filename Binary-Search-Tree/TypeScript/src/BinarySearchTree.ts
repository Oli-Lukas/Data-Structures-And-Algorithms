import Node from './Node';

export default class BinarySearchTree {
  root: Node | null;

  constructor() {
    this.root = null;
  }

  insert(value: number): void {
    const newNode = new Node(value);

    if (this.root === null) {
      this.root = newNode;
    } else {
      let current = this.root;

      while (true) {
        if (value === current.value) {
          return;
        }

        if (value < current.value) {
          if (current.left === null) {
            current.left = newNode;
            return;
          }
          current = current.left;

        } else {
          if (current.right === null) {
            current.right = newNode;
            return;
          }
          current = current.right;

        }
      }     
    }
  }

  search(value: number): Node | null {
    let current = this.root;

    while (current !== null) {
      if (value === current.value) {
        return current;
      }

      if (value < current.value) {
        current = current.left;
      } else {
        current = current.right;
      }
    }

    return null;
  }
}