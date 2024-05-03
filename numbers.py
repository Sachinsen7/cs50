import sys

numbers = [4, 5, 8, 9, 0, 2, 3]

if 5 in numbers:
    print("Found")
    sys.exit(0)

print("Not Found")
sys.exit(1)