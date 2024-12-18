students = []

with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["house"] = house
        student = {"name":name, "house":house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key = get_house):
    print(f"{student['name']} is in {student['house']}")  

for student in sorted (students, key = lambda student: student["house"]):
    print(f"{student['name']} is in {student['house']}")
    