from typing import Optional
from node import Node

class BinarySearchTree:
  def __init__(self) -> None:
    self.root: Optional[Node] = None
  
  def insert(self, value: int) -> None:
    new_node: Node = Node(value)

    if self.root is None:
      self.root = new_node
    else:
      current: Optional[Node] = self.root

      while True:
        if value == current.value:
          return
        
        if value < current.value:
          if current.left is None:
            current.left = new_node
            return
          
          current = current.left
        else:
          if current.right is None:
            current.right = new_node
            return
          
          current = current.right
  
  def search(self, value: int) -> Optional[Node]:
    current: Optional[Node] = self.root

    while current is not None:
      if value == current.value:
        return current
      
      if value < current.value:
        current = current.left
      else:
        current = current.right
    
    return None
