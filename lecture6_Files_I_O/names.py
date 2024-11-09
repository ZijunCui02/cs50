name = input("What's your name? ")

# file = open("name.txt", "a") # store the name
# "w": rewrites the file
# "a": append

with open("name.txt", "a") as file:
    file.write(f"{name}\n")

# file.write(name)
# file.write("\n")
#file.close()

