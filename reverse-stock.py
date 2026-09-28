
def reserve_stock(stock, order):
    requested = {}
    remaining = stock.copy()
    for item, quantity in order:
        if item not in stock:
            raise ValueError("unknown item")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        requested[item] = requested.get(item, 0) + quantity
        if requested[item] > stock[item]:
            raise ValueError("insufficient stock")
    remaining = stock.copy()


    for item, quantity in requested.items():
        remaining[item] = stock[item] - quantity
    return remaining

stock = {"pen": 5}
try:

      result = reserve_stock(stock, [("pen", 3), ("pen", 3)])
      assert False, "expected ValueError"
except ValueError:
    assert stock == {"pen": 5}

stock = {"pen": 10}
result = reserve_stock(stock, [("pen", 3), ("pen", 4)])
assert result == {"pen": 3}
assert stock == {"pen": 10}