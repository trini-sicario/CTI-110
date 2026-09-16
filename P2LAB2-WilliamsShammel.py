# Williams Shammel
# 16 September 2026
# Use dictionaries to determine fuel needed

# Create a dictionary where keys are car names & values are MPG
Cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

# Display the dictionary
print(Cars.keys())

# Get name of car from user
car_name = input("Enter the name of the car: ")

# Pull the MPG associated with the car name
mpg_car = Cars[car_name]

print()
# Display the MPG of the selected car
print(f"The {car_name} gets {mpg_car} mpg.")

print()
# Get the distance the user plans to drive  
distance = float(input(f"How many miles will you drive the {car_name}?"))

print()
# Calculate the fuel needed for the trip 
fuel_needed = distance/mpg_car 

# Display the fuel needed for the trip
print(f"You will need {fuel_needed:.2f} gallons of fuel needed to drive the {car_name} for {distance} miles.")

