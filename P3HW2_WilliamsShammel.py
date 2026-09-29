# Williams, Shammel
# 28 September 2026
# Salary calculator

# request employee information
name = input("Enter employee name: ")
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

# Evaluate overtime pay
if hours > 40:
    # calculate overtime pay
    overtime_hours = hours - 40
    # calculate over pay rate
    overtime_pay = overtime_hours * (rate * 1.5)
    # calculate salary for regular hours
    regular_pay = 40 * rate
    # calculate gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay
    
# Display results
print("-------------------------------------------------------------------")
print(f"Employee Name: {name}")
print(f'{"Hours Worked":<15}{"Pay rate":<12}{"OvertTime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<15}')
print("-------------------------------------------------------------------")
print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')
