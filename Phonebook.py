people = {
    "carter": "+918718857168",
    "David": "+914785126856"
}

name = str(input("Name: "))
if name in people:
    number = people[name]
    print(f"Number: {people[name]}")



import csv

file = open("Phonebook.csv", "a")

name = str(input("Name: "))
number = str(input("Number: "))

writer = csv.writer(file)
writer.writerow([name, number])

file.close()

