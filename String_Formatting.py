# Learn to format strings in Python using f-strings

num_dogs = 10
num_hamsters = 6
num_fishes = 9
num_butterflies = 12

dogs_cost = 150.00
hamsters_cost = 25.00
fishes_cost = 250.00
butterflies_cost = 5.50

print(f"======{'Animal type':^26}{'Number available':^26}{'Cost':^26}======")
print("-" * 90)
print(f"{'Dogs':<26}{num_dogs:^26}{dogs_cost:^26.2f}")
print(f"{'Hamsters':<26}{num_hamsters:^26}{hamsters_cost:^26.2f}")
print(f"{'Fishes':<26}{num_fishes:^26}{fishes_cost:^26.2f}")
print(f"{'Butterflies':<26}{num_butterflies:^26}{butterflies_cost:^26.2f}")