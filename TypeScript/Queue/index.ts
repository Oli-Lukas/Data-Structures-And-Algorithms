import Queue from './Queue';

const myQueue = new Queue<string>();

myQueue.enqueue('foo');
myQueue.enqueue('bar');

console.log(myQueue.peek());
console.log(myQueue.dequeue());
console.log(myQueue.size());
console.log(myQueue.isEmpty());