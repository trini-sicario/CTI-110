# Helper file for P2HW2

# Get three Prices from the user
price1 = float(input("Enter price of the first item: "))
price2 = float(input("Enter price of the second item: "))
price3 = float(input("Enter price of the third item: "))

# Create a list of the input variables
prices = [price1, price2, price3]

# If list is all ints and floats, there are, functions you can call on the list

# Sum function adds all list tiems together
print(sum(prices))

# Min function returns the lowest value in the list
min_value = min(prices)
print(f"The lowest price is: {min_value}")

# Max function returns the highest value in the list
max_value = max(prices)
print(f"The highest price is: {max_value}")

# Calculate the average of the prices
avg_price = sum(prices) / len(prices)
print()
print(f"The average price is: ${avg_price:.2f}")

