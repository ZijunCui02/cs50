with open("students.csv") as file:
    for line in file:
        # row =[]
        # row = line.rstrip().split(",") # list
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

 