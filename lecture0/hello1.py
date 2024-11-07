############################################
#hash for comment

############################################
# pseudocode
# input name
# print "Hello" + name
# end
############################################

# Ask user for their name
name = input("What's your name? ")
# Say hello to the user
print("Hello " + name + "!")
############################################

# + for no space
# , for space
############################################

print("Hello, ",end="")# Overwrtie end
print(name,name, sep="???")# Overwrite sep

#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#objects - object to the printed. * indicates that there may be more than one object
#sep - objects are separated by sep. Default is space
#end - end is printed at last

############################################
print('hello, "friend"')
print("hello, \"friend\"")

print(f"hello, {name}")

############################################
name = name.strip().title()
# strip() removes leading and trailing spaces
# title() makes first letter of each word capital
# or. capitalize() makes first letter of first word capital
print(f"hello, {name}")

