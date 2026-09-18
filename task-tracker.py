from collections import deque

class TaskScheduler:
    def __init__(self):
        self.queue = deque()        # order tasks are waiting to run
        self.task_lookup = {}       # id -> description (O(1) lookup)
        self.completed_stack = []   # most recently completed on top

    def add_task(self, task_id, description):
        self.queue.append(task_id)
        self.task_lookup[task_id] = description
        print(f"Added: [{task_id}] {description}")

    def complete_next(self):
        if not self.queue:
            print("No tasks in queue.")
            return None
        task_id = self.queue.popleft()          # take from front (FIFO)
        self.completed_stack.append(task_id)     # push onto undo stack
        print(f"Completed: [{task_id}] {self.task_lookup[task_id]}")
        return task_id

    def undo_last_complete(self):
        if not self.completed_stack:
            print("Nothing to undo.")
            return None
        task_id = self.completed_stack.pop()          # take most recent (LIFO)
        self.queue.appendleft(task_id)                 # put back at front of queue
        print(f"Undone: [{task_id}] {self.task_lookup[task_id]} — back in queue")
        return task_id

    def show_queue(self):
        print("Queue:", [f"{tid}:{self.task_lookup[tid]}" for tid in self.queue])

    def show_completed(self):
        print("Completed (most recent last):", 
              [f"{tid}:{self.task_lookup[tid]}" for tid in self.completed_stack])


# --- Demo ---
scheduler = TaskScheduler()
scheduler.add_task(1, "Write API docs")
scheduler.add_task(2, "Fix login bug")
scheduler.add_task(3, "Review PR")

scheduler.show_queue()

scheduler.complete_next()   # completes task 1
scheduler.complete_next()   # completes task 2
scheduler.show_queue()
scheduler.show_completed()

scheduler.undo_last_complete()   # undoes task 2, back in queue
scheduler.show_queue()
scheduler.show_completed()