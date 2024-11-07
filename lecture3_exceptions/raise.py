def divide(x, y):
    if y == 0:
        raise ValueError("The divisor cannot be zero.")
    return x / y

def main():
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        result = divide(x, y)
    except ValueError as e:
        print(e)
    else:
        print(f"{x} divided by {y} is {result}")
        
main()