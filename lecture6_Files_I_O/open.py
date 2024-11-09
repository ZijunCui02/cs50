# "r" is the implicit default

with open ("name.txt", "r") as file :
    for line in file:
        print("hello", line.rstrip())
#     lines = file.readlines() # return as a list: lines

# for line in lines:
#     # print("hello,", line, end ="")
#     print("hello,", line.rstrip())
    


