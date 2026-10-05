from collections import deque

queue = deque()
queue.append("Customer 1")    # joins at the back
queue.append("Customer 2")
queue.append("Customer 3")


print(queue.popleft())        # removes from the front