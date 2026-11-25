print("Student Result Calculator")

# Get marks from the student
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))


# Validate marks
if not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
    print("Invalid marks. Enter marks between 0 and 100.")
    exit()

# Calculate average
average = (m1 + m2 + m3) / 3

# Display result
print("Average marks:",round(average,2))

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Letter grade:", grade)

# Determine pass or fail status
if average >= 60:
    print("Status: Pass")
else:
    print("Status: Fail")
