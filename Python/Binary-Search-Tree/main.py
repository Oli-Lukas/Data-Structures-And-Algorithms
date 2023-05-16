from typing import Optional
from binary_search_tree import BinarySearchTree

tree: BinarySearchTree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(20)

print(tree.search(7))
print(tree.search(10))
print(tree.search(18))