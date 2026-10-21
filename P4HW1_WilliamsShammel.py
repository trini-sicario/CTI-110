# Williams Shammel
# 21 October 2026
# Nested loops to input and validate grades

# make an empty list to hold the grades
from unittest import result


grades_list = []

num_of_grades = int(input("How many grades will you enter? ")) # Get user input for number of grades

# for loop that gets one grade for each interaction
for i in range(1, num_of_grades + 1):
    grade = float(input(f"Enter grade #{i}: ")) # get the grade from the user
    
    # while the input is not valid, keep asking for a valid grade
    while grade < 0 or grade > 100:
        print("Invalid grade. Please enter a grade between 0 and 100.")
        grade = float(input(f"Enter grade #{i} again: ")) # ask the user to reenter the grade
    # while loop breaks when a valid grade is entered
    grades_list.append(grade) # add the valid grade to the list
    
print("----------------result----------------")
print("Lowest grade:", min(grades_list)) # print the lowest grade
print("Highest grade:", max(grades_list)) # print the highest grade
print("Score Average:", sum(grades_list) / len(grades_list)) # print the average grade
print("Grades entered:", grades_list) # print the list of grades
