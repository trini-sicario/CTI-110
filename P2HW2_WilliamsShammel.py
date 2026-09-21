# Williams, Shammel
# 21 September 2026
#Assignment assess student understanding of Lists
#create a program that will ask the user to enter test grades for 6 modules. The program should then display the lowest grade, the highest grade, the sum of all grades, and the average of all grades.

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