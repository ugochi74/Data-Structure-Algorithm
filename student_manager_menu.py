import copy


students = {
    "John": [70, 80, 90],
    "Mary": [85, 90, 95],
    "Peter": [60, 75, 70]
}



def calculate_average(scores):
    return sum(scores) / len(scores)

def add_score(students_data, students_name, score):
    students_data[students_name].append(score)

def create_backup(students_data):
    return copy.deepcopy(students_data)
#assert calculate_average(students["john"]) == 80

# 5. DEFINE run_tests HERE
def run_tests():

    assert calculate_average([70, 80, 90]) == 80
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([100, 100, 100]) == 100

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

backup = None
while True:

    print("\n===== STUDENT MANAGER =====")
    print("1. Show students")
    print("2. Add score")
    print("3. Calculate average")
    print("4. Create backup")
    print("5. Test program")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        for name, scores in students.items():
            print(name, ":", scores)

    elif choice == "2":

        name = input("Enter student name: ")
        score = int(input("Enter score: "))

        students[name].append(score)

        print("Score added successfully!")

    elif choice == "3":

        name = input("Enter student name: ")

        if name not in students:
            print("Student not found!")
            continue

        average = calculate_average(students[name])

        print(name, "average:", average)


    # OPTION 4: CREATE BACKUP

    elif choice == "4":

        backup = create_backup(students)

        print("Backup created successfully!")

    # OPTION 5: RUN TESTS

    elif choice == "5":

        run_tests()

    # OPTION 6: EXIT

    elif choice == "6":

        print("Goodbye!")
        break

    # INVALID OPTION

    else:

        print("Invalid option. Please choose 1-6.")