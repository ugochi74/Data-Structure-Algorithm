numbers = [5, 2, 8, 1, 9]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)