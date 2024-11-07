def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to="world"):
    to=to.strip().title()
    print(f"hello, {to}")

main()

# scope only exists in the sytax of the function