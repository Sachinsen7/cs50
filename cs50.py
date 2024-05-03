try:
    x = int(input("x: "))
except ValueError:
    print("that is not an int!")
    exit()
try:
    y = int(input("x: "))
except ValueError:
    print("that is not an int!")
    exit()
print(x + y)


x = int(input("x: "))
y = int(input("y: "))

z = x / y
#USE // FOR INT VALUE

#This is a comment
print(f"{z:.50f}")   #use z only

