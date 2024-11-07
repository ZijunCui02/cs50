functions
arguments
side effects
bugs
return values
vairables
pseudocode
multi-function arguments

str

postional print

named parameters: end, sep optional

# Hash symbol
# Ask user for their name
name = input ("What's your name? ")#string (text)

# Remove whitespace from str and capitalize user's name
# name = name.strip()
# name = name.capitalize() # caplitalize first letter
# name = name.title() # caplitalize every first letter
name = name.strip().title()

code=1
"""
multiple line comments -- have special meaning
"""
#Say hello to user
print("hello,", name+"!",code)# use + 

# multi-function arguments, use comma, automatically add one space
#overwrite end
print("hello, ", end="")
print(name)
# overwrite sep
print("hello,", name, sep="???")

#print a quote
print("\'")
print('hello, "friend"')
print(f"hello, {name}, {code}") #format

"""
multiple line comments -- have special meaning
"""

interger

float

