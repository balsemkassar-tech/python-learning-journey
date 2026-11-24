
# Student Grade Manager

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


print("\n===== STUDENT RESULTS =====")

for student in students:
    print("Name:", student["name"])
    print("Grades:", student["grades"])
    print("Average:", round(student["average"], 2))


best_student = max(students, key=lambda s: s["average"])

print("\nBest student:", best_student["name"])
print("Highest average:", round(best_student["average"], 2))
