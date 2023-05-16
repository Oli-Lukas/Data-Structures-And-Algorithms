from typing import TypeVar, Generic, List

T = TypeVar('T')

class Queue(Generic[T]):
  def __init__(self) -> None:
    self.items: List[T] = []
  
  def enqueue(self, item: T) -> None:
    self.items.append(item)
  
  def dequeue(self) -> T:
    return self.items.pop(0)
  
  def is_empty(self) -> bool:
    return len(self.items) == 0
  
  def peek(self) -> T:
    return self.items[0]
  
  def size(self) -> int:
    return len(self.items)
