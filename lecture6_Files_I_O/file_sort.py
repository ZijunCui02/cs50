with open("name.txt") as file:
    for line in sorted(file, reverse=True):
        print(f"hello,{line.rstrip()}")
        