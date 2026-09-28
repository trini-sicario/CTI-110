# Williams, Shammel
# 28 September 2026
# Branching and Lists
# build on your work from P2HW2 that covered Python lists.

print("Enter test grades for the following modules:")
module1 = float(input("Enter grade for module 1: "))
module2 = float(input("Enter grade for module 2: "))
module3 = float(input("Enter grade for module 3: "))
module4 = float(input("Enter grade for module 4: "))
module5 = float(input("Enter grade for module 5: "))
module6 = float(input("Enter grade for module 6: "))

# Create a list of module grades
grades = [module1, module2, module3, module4, module5, module6]

print("-----------Results-----------")

# Display the lowest grade
print(f"The lowest grade is: {min(grades)}")

# Display the highest grade
print(f"The highest grade is: {max(grades)}")

# Display the sum of all grades
print(f"The sum of all grades is: {sum(grades)}")


# Display the average of all grades
print(f"The average of all grades is: {sum(grades) / len(grades):.2f}")

print("-------------------------------------")

average = sum(grades) / len(grades)
# Determine the letter grade based on the average
if average >= 90:
    letter_grade = "A"
if average >= 80 and average <= 89:
    letter_grade = "B"
if average >= 70 and average <= 79:
    letter_grade = "C"
if average >= 60 and average <= 69:
    letter_grade = "D"
if average <= 59:
    letter_grade = "F"

# Display the letter grade
print(f"Your letter grade is: {letter_grade}")