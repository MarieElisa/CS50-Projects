import csv

studentslist = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        studentslist.append({"name": row["name"], "home": row["home"]})

for student in sorted(studentslist, key=lambda student: student["name"]):
    print(f"{student['name']} is at {student['home']}")