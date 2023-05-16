import BinarySearchTree from "./BinarySearchTree";

const tree = new BinarySearchTree();

tree.insert(10);
tree.insert(5);
tree.insert(15);
tree.insert(2);
tree.insert(7);
tree.insert(12);
tree.insert(20);

console.log(tree.search(7));
console.log(tree.search(10));
console.log(tree.search(18));