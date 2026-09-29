student = {"name": "John", "age": 20}

student["grade"] = "A"             # insert: O(1)
student["age"] = 21                # update: O(1)
print(student["name"])             # lookup: O(1), KeyError if missing
print(student.get("email"))        # None if missing, no error
print(student.get("email", "n/a")) # custom default
print("age" in student)            # membership test: O(1)
del student["grade"]               # delete: O(1)
student.pop("age", None)           # delete without KeyError

for k, v in student.items():
    print(k, v)