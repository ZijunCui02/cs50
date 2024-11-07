# sys # system
import sys # sys.argv command-line prompt

try:
    print("hello, my name is",sys.argv[1])
except IndexError:
    pass
print("hello, my file name is", sys.argv[0])

# (base) @ZijunCui02 ➜ /workspaces/codespaces-blank $ python name.py harry
# hello, my name is harry
# hello, my file name is name.py

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many argument")
# else:
#     print("hello, my name is", sys.argv[1])

for arg in sys.argv[1:-1]: # slice
    print ("Hello, my name is", arg)
    