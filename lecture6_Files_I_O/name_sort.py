names = []

with open("name.txt") as file:
    # names = file.readlines()
    for line in file: 
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

