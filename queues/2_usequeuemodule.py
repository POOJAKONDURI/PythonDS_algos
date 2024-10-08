import queue

q = queue.Queue()

# Enqueue elements
q.put(10)
q.put(20)

# Dequeue elements
print(q.get())  # Output: 10

# Check if queue is empty
print(q.empty())  # Output: False
