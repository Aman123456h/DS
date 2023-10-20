#List ADT
list=[10,20,30,"Mumbai","Chennai"]
print("List elements are:", list)
list.append(40)
list.append(50)
list.append("New Delhi")
print("List elements:", list)
list.pop();
print("List elements:", list)
list.pop();
print("List elements:", list)

#Stack Using List
stack = []
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack')
print(stack)
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are popped:')
print(stack)

# Queue Using List

queue = []
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)