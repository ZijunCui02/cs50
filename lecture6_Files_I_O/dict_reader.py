import csv

students = []

with open("home.csv") as file:
    # DictReader returns a dictionary 
    reader = csv.DictReader(file) 
    for row in reader:
        students.append({"name": row["name"], "home": row["home"], "house": row["house"]})
print(reader.fieldnames)

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']} at {student['house']}")
