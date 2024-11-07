students = ["Hermione","Harry","Ron"]

for i in range(3):
    print(students[i])
    
for student in students:
    print(student)
    
for i in range(len(students)):
    print(i+1,students[i])
    
### dict ###
### associate key with value ###

# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor","Gryffindor", "Slytherin"]

### Using Python Dict ###
### {} ###

print("\n")

students = {
    "Hermione": "Grynffindor","no": "yes",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
print(students["Hermione"]+"\n")

for student in students:
    print(student,students[student],sep=', ')

# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor","Gryffindor", "Slytherin"]
# patronus = ["Otter", "Stag", "Jack Russel terrier"]

students= [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

print(students,"\n")

for student in students:
    print(student)

print("\n")

for student in students:
    print(student["name"],student["house"],student["patronus"],"\n",sep=", ")
    