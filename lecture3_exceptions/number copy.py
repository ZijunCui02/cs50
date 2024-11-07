def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x # return int(input("What's x?"))
        except ValueError:
            # pass
            print("x is not an integer")
        # else: # only do if try succeeded
            # #break
            # return x # return is more powerful than break

def main():
    x = get_int("What's x?")
    print(f"x is {x}")

main()

### try
### except
# more elegantly