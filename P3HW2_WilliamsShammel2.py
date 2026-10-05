# Williams, Shammel
# 28 September 2026
# Use if else statements to determine weekly pay with and without overtime pay


import streamlit as st
# run command: python -m streamlit run P3HW2_Williamsshammel.py

# make title on our UI
st.title("Weekly Paycheck Calculator 💵💴")

# request employee information
name = st.text_input("Enter employee name: ")

# Get number of hours worked
hours_worked = st.number_input("Enter hours worked for one week: ", min_value=0.0, step=0.1)

# Get regular pay rate
rate = st.number_input("Enter base rate: ", min_value=0.0, step=0.01)

#----------Evaluate overtime pay---------------------
if hours_worked > 40:
    # calculate overtime pay
    overtime_hours = hours_worked - 40
    # calculate over pay rate
    overtime_pay = overtime_hours * (rate * 1.5)
    # calculate salary for regular hours
    regular_pay = 40 * rate
    # calculate gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours_worked * rate
    gross_pay = regular_pay
    
#----------Display results----------------------------
st.write("-------------------------------------------------------------------")
st.write(f"Employee Name: {name}")
st.write()
st.write(f"Hours Worked: {hours_worked:.2f}")
st.write(f"Pay rate: {rate:.2f}")
st.write(f"OvertTime Pay: ${overtime_pay:.2f}")
st.write(f"Regular Pay: ${regular_pay:.2f}")
st.write(f"Gross Pay: ${gross_pay:.2f}")
