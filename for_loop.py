# A simple for loop in Python
# 12 October 2026
# This program demonstrates a basic for loop that iterates over a list of numbers and prints each number.

# '''....''' THE QUOTE SYMBOLS ARE USED TO COMMENT OUT MULTIPLE LINES OF CODE IT IS CALLED A MULTI-LINE COMMENT. IT IS NOT A STRING.'''
# For loop that iterates 5 times

import time
'''
# Range never includes the last value
# Range(start, stop, step) (exp. start at 2, stop at 11, count by 2)
for s in range(2,11,2):
    print(s)
    time.sleep(2)
    
# loop breaks here
print("Loop has completed.")
'''

# CREATE A LIST
fRIENDS = ["Alice", "Bob", "Charlie", "David", "Eve", "Mell"]

# Loop to display each friend with an emoji
print("Here are my friends:")
for friends_name in fRIENDS:
    print(friends_name + "😎")
    time.sleep(2)
    
# loop breaks here
print("Loop has completed.")