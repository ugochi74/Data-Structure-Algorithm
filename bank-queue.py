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





def bank_simulation():
    line = Queue()

    customers = ["Customer 1", "Customer 2", "Customer 3"]
    for customer in customers:
        line.enqueue(customer)
        print(f"{customer} joined the line.")

    print("\n--- Serving customers ---")
    while not line.is_empty():
        being_served = line.dequeue()
        print(f"Now serving: {being_served}")

bank_simulation()