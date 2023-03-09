from queue import Queue

my_queue = Queue[str]()

my_queue.enqueue('foo')
my_queue.enqueue('bar')

print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.size())
print(my_queue.is_empty())