import math
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    print(f"Square root of x is {squared(x):.2f}")
    
def squared(x):
    return math.sqrt(x)
    
def square(x):
    return x**2
    #return pow(x,2)
    #return math.pow(x,2)

main()