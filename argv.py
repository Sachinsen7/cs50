from sys import argv

if len(argv) == 2:
    print(f"Hello, {argv[1]}")
else:
    print("Hello, world")

for arg in argv:
    if arg != "argv.py":
     print(arg)

for arg in argv[1:]:
    print(arg)                            #go to terminal window and type python argv.py fo baz zaz


