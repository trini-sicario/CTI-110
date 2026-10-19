# Williams Shammel
# October 19 2026
# use nested loops

# create a variable so the wile loop is true first iteration
run_again ="yes"

# while  loop that is true when runb-again equals yes
while run_again == "yes":
    print("program is running")
    print()
    # Get integer input from user
    user_int = int(input("Enter an integer: "))
    
    if user_int >=0: # Determine if user_int is positive or negative
        print("number is positive")
        for i in range(1,13):
            print(f"{user_int} * {i} = {user_int * i}") # print the multiplication table for user_int
    else:
        print("Program does not handle negative numbers")
    
    
    run_again = input("run the program again? (yes/no): ").lower() #Ask user if they want to run again 
    
# loop has broken and the program is done running
print("Thats whats up the program is done, take it easy out there.....PEACE!!")