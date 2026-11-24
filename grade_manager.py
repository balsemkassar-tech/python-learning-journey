
import json

students = []

number = int(input("How many students? "))

for i in range(number):
    print("\nStudent", i + 1)

    name = input("Name: ")
    grades = []

    for j in range(3):
        grade = float(input("Grade " + str(j + 1) + ": "))
        grades.append(grade)

    average = sum(grades) / 3

    student = {
        "name": name,
        "grades": grades,
        "average": average
    }

    students.append(student)

# Display results
print("\n===== STUDENT RESULTS =====")

for student in students:
    print("Name:", student["name"])
    print("Average:", round(student["average"], 2))

# Find best student
best_student = max(students, key=lambda s: s["average"])

print("\nBest student:", best_student["name"])

# Save data to JSON file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nStudent data saved successfully!")
