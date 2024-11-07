def get_int():
    
    while True:
        try:
            x = int(input("What's x?"))
            return x # return int(input("What's x?"))
        except ValueError:
            # pass
            print("x is not an integer")
        # else: # only do if try succeeded
            # #break
            # return x # return is more powerful than break

def main():
    x = get_int()
    print(f"x is {x}")

main()

### try
### except
# more elegantly
