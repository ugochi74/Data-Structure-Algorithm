from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add an item to the back of the line."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the line."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self):
        """Look at the next item in line, without removing it."""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

line = Queue()

line.enqueue("Customer 1")
line.enqueue("Customer 2")
line.enqueue("Customer 3")

print(line.front())      # "Customer 1" — next to be served, still in line
print(line.dequeue())    # "Customer 1" — now actually removed/served
print(line.dequeue())    # "Customer 2"
print(line.front())      # "Customer 3" — only one left