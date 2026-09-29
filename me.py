
def walk(path, depth):
    if depth == 3:
        print(path)
        return
    for choice in ["L", "R"]:
        path.append(choice)      # choose
        walk(path, depth + 1)    # explore
        #path.pop()               # undo

walk([], 0)