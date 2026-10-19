# Simulating a clock with nested loops

hours = 0
minutes = 0

for h in range(1,13):  # Loop for hours

    for m in range(60):  # Loop for minutes
        if m < 10:
            print(f"{hours}:0{m}")  # Format minutes to have leading zero if less than 10
        else:
            print(f"{hours}:{m}")

    # add one to the hours after every 60 minutes
    hours += 1