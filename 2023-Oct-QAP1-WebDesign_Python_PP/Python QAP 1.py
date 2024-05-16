# =============================================================================
# Project 2 - Python Program (5 Points)
# Date:   Sept 14, 2023
# Author: David Husk Jr
# Email:  dave.husk@keyin.com
# =============================================================================

# -----------------------
# Import Required Modules
# -----------------------
import datetime

# Welcome Message
print("# =============================================================================")

# Display Current Date and Time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Current Date and Time: {current_time}")

# Initial Constants
COMPANY_NAME = "Edsel Car Rental Company"
DAILY_RENTAL_RATE = 55.00
COST_PER_KM = 0.24
INSURANCE_RATE = 14.00
RENTAL_DISCOUNT = 10  # In percentage
MILEAGE_DISCOUNT = 25  # In percentage
HST_RATE = 15  # In percentage

# Display Constants and Allow User to Modify Them
print("\n==================== Constants ====================")
print(f"1. Company Name: {COMPANY_NAME}")
print(f"2. Daily Rental Rate: ${DAILY_RENTAL_RATE}")
print(f"3. Cost Per KM: ${COST_PER_KM}")
print(f"4. Insurance Rate: ${INSURANCE_RATE}")
print(f"5. Rental Discount: {RENTAL_DISCOUNT}%")
print(f"6. Mileage Discount: {MILEAGE_DISCOUNT}%")
print(f"7. HST Rate: {HST_RATE}%")
print("====================================================")

# Function to safely update a constant
def update_constant(prompt, current_value):
    while True:
        try:
            new_value = input(prompt)
            if new_value == "":
                return current_value
            new_value = float(new_value)
            return new_value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Update Constants if Necessary
COMPANY_NAME = input(f"Enter new company name or press Enter to keep '{COMPANY_NAME}': ") or COMPANY_NAME
DAILY_RENTAL_RATE = update_constant(f"Enter new daily rental rate or press Enter to keep ${DAILY_RENTAL_RATE}: ", DAILY_RENTAL_RATE)
COST_PER_KM = update_constant(f"Enter new cost per KM or press Enter to keep ${COST_PER_KM}: ", COST_PER_KM)
INSURANCE_RATE = update_constant(f"Enter new insurance rate or press Enter to keep ${INSURANCE_RATE}: ", INSURANCE_RATE)
RENTAL_DISCOUNT = update_constant(f"Enter new rental discount rate in percentage or press Enter to keep {RENTAL_DISCOUNT} %: ", RENTAL_DISCOUNT)
MILEAGE_DISCOUNT = update_constant(f"Enter new mileage discount rate in percentage or press Enter to keep {MILEAGE_DISCOUNT} %: ", MILEAGE_DISCOUNT)
HST_RATE = update_constant(f"Enter new HST rate in percentage or press Enter to keep {HST_RATE} %: ", HST_RATE)

# Convert percentages to decimals for calculations
RENTAL_DISCOUNT /= 100
MILEAGE_DISCOUNT /= 100
HST_RATE /= 100

# Rest of the code for user input and calculations
# ...




# -----------------------
# Welcome Message
# -----------------------

print("##################################################")
print(f"# Welcome to {COMPANY_NAME}")
print("#   - Rental Car Cost Calculator")
print("##################################################")

# -----------------------
# User Input
# -----------------------

# Collect customer details and rental information
customer_name = input("# Customer Name:                ")
phone_number = input("# Customer Phone #:             ")
days_rented = int(input("# Day(s) with rental:           "))
odometer_start = int(input("# Odometer Start (5 digits):    "))
odometer_end = int(input("# Odometer Returned (5 digits): "))

# -----------------------
# Calculations
# -----------------------

# Calculate total kilometers traveled
km_traveled = odometer_end - odometer_start

# Calculate various costs
rental_cost = days_rented * DAILY_RENTAL_RATE
mileage_cost = km_traveled * COST_PER_KM
insurance_cost = days_rented * INSURANCE_RATE

# Calculate discounts
rental_discount = rental_cost * RENTAL_DISCOUNT
mileage_discount = mileage_cost * MILEAGE_DISCOUNT
total_discount = rental_discount + mileage_discount

# Calculate total rental cost
total_rental_cost = rental_cost + mileage_cost + insurance_cost - total_discount

# Calculate HST
hst = total_rental_cost * HST_RATE

# Calculate final invoice total
final_invoice = total_rental_cost + hst

# -----------------------
# Display Results
# -----------------------

# Display the invoice with a structured layout
print("# ")
print("##################################################")
print(f"# CUSTOMER # {customer_name}")
print(f"#   PHONE  # {phone_number}")
print("##################################################")
print(f"# ODOMETER    (Start: {odometer_start} KM / End: {odometer_end} KM )")
print(f"#  {km_traveled} KM")
print("# ")
print(f"# RENTAL PERIOD     {days_rented} day(s)")
print(f"#              Cost: ${rental_cost}")
print(f"#           Mileage: ${mileage_cost}")
print(f"#         Insurance: ${insurance_cost}")
print(f"#                  - ${total_discount} Discount")
print("#                    ======")
print(f"#   Sub-Total:       ${total_rental_cost}")
print(f"#                  + ${hst} HST")
print("#                    ________________________")
print(f"# Closing Balance:   ${final_invoice}")
print("##################################################")
