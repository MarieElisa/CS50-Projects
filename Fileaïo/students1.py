import csv

studentslist = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        studentslist.append({"name": name, "home": home})

for student in sorted(studentslist, key=lambda student: student["name"]):
    print(f"{student['name']} is at {student['home']}")