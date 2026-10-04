class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


class UndoRedoEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()
    # ... rest stays the same




class UndoRedoEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def type(self, new_text):
        self.undo_stack.push(self.text)   # save current state before changing
        self.text = new_text
        self.redo_stack = Stack()         # new action invalidates redo history
        print(f"Type: {self.text}")

    def undo(self):
        if self.undo_stack.is_empty():
            print("Nothing to undo.")
            return
        self.redo_stack.push(self.text)        # save current state for redo
        self.text = self.undo_stack.pop()      # go back
        print(f"Undo\n→ {self.text}")

    def redo(self):
        if self.redo_stack.is_empty():
            print("Nothing to redo.")
            return
        self.undo_stack.push(self.text)        # save current state for undo
        self.text = self.redo_stack.pop()      # go forward
        print(f"Redo\n→ {self.text}")


# --- Demo, matching your curriculum's expected output ---
editor = UndoRedoEditor()
editor.type("white")
editor.type("blue")
editor.type("red")
editor.type("green")
# editor.type("Hello")
# editor.type("Hello world")
# editor.type("Hello world")

editor.undo()   # Hello World
editor.undo()   # Hello
editor.redo()   # Hello World
editor.redo()
