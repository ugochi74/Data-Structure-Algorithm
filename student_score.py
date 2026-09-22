import copy


students = {
    "john": [70, 80, 90],
    "mary": [85, 90, 95],
    "peter": [60, 75, 70]
}


def calculate_average(scores):
    return sum(scores) / len(scores)

def add_score(students_data, students_name, score):
    students_data[students_name].append(score)

def create_backup(students_data):
    return copy.deepcopy(students_data)
#assert calculate_average(students["john"]) == 80
assert calculate_average([70, 80, 90]) == 80
assert calculate_average([10, 20, 30]) == 20
assert calculate_average([100, 100, 100]) == 100
assert calculate_average([50, 60]) == 55



test_students = {
    "John": [70, 80, 90]
}

add_score(test_students, "John", 100)

assert test_students["John"] == [70, 80, 90, 100]


original = {
    "John": [70, 80, 90]
}

backup = create_backup(original)

backup["John"].append(100)

assert original["John"] == [70, 80, 90]

assert backup["John"] == [70, 80, 90, 100]


print("All tests passed!")

#backup = students.copy()
#backup = copy.deepcopy(students)