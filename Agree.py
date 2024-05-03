s = str(input("Do you agree? ")).lower()

if s in ["y" , "yes"]:    # use s.lower() in
    print("Agreed.")
elif s in ["n", "no"]:
    print("Not Agreed.")