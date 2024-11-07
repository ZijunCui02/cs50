# while True:
#     n = int(input("Number: "))
#     if n >0:
#         break # continue

# for _ in range(n):
#     print("meow")
    

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Number:"))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")
main()