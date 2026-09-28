# Branching (if/else/elif) statements are used to control the flow of a program based on certain conditions. They allow you to execute different blocks of code depending on whether a condition is true or false.

# Get users age 
age = int(input("Enter your age: "))

# determine if the age is greater or equal to 65
if age >= 65:
    print("you are a senior citizen.")
    discount = 0.40
    
else:
    print("you are not a senior citizen.")
    discount = 0.0
    
print("You made a purchase of $100.00")
print("Discount applied: ${:.2f}".format(discount * 100))