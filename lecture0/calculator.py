x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x+y,5)
zz = round( x/y, 3)
#int() not only type, but also function
print(z)
print(f"{z:,}")
print(f"{z:.2f}")

print(round(x/y,3))
print(f"{zz:.2f}")


