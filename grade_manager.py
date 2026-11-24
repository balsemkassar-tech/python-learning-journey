
# Student Grade Manager

print("===== STUDENT GRADE MANAGER =====")

# Get student information
name = input("Enter student name: ")

# Get three grades
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))

# Calculate average
average = (grade1 + grade2 + grade3) / 3

# Display results
print("\n===== RESULTS =====")
print("Student:", name)
print("Average:", round(average, 2))
