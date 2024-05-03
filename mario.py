while True:
   n = int(input("Height: "))
   if n > 0:
       break

for i in range(n):
    print("#")

def main():
    height = get_height()
    for i in range(height):
        print("#")

def get_height():
    while True:
        n = int(input("Height: "))
        if n > 0:
            break
    return n

main()

def main():
    height = get_height()
    for i in range(height):
        print("#")

def get_height():
    while True:
        try:
           n = int(input("Height: "))
           if n > 0:
               break
        except:
            print("That is not an integer:")
    return n

main()