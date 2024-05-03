before = str(input("Before: "))
print("After: ", end="")
for c in before:
    print(c.upper(), end="")
print()
                                  #same as bottom it will do the same thing

before = str(input("Before: "))
after = before.upper()
print(f"After: {after}", end="")
print()

before = str(input("Before: "))
print(f"After: {before.upper()}")