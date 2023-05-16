from typing import Optional

class Node:
  def __init__(self, value: int) -> None:
    self.value: int = value
    self.left : Optional[Node] = None
    self.right: Optional[Node] = None
