# Ask user for their name
name = input ("What's your name? ").strip().title()
code=1

#Split user's name into first name and last name

first, last = name.split(" ")

#Say hello to user
print("Hello,", name+"!")
print(f"hello,{first}!")
