import datetime

# =============================================================================
#                               Rental Car Cost Calculator
# -----------------------------------------------------------------------------
#  Author:   David Husk Jr
#  Email:    dave.husk@keyin.com
#  Due Date: 2023-09-19 14:13:!5
# -----------------------------------------------------------------------------
#  This program calculates the cost of renting a car. It allows the user to
#  modify certain constants to tailor the calculation to specific scenarios.
# =============================================================================

# -----------------------
#  Initial Configuration
# -----------------------

# Constants
COMPANY_NAME       = "Edsel Car Rental Company"
DAILY_RENTAL_RATE  = 55.00
COST_PER_KM        = 0.24
INSURANCE_RATE     = 14.00
RENTAL_DISCOUNT    = 10  # In percentage
MILEAGE_DISCOUNT   = 25  # In percentage
HST_RATE           = 15  # In percentage

# Display Current Date and Time
print(f"\nCurrent Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Ask if User Wants to Change Constants
change_constants = input("\nWould you like to change any constants? (yes/no): ").strip().lower()

if change_constants == 'yes':
    # Display Constants in a Table
    print("\n==================== Constants ====================")
    print(" No | Constant Name     | Current Value")
    print("----|-------------------|--------------")
    print("  1 | Company Name      |", COMPANY_NAME)
    print(f"  2 | Daily Rental Rate | ${DAILY_RENTAL_RATE}")
    print(f"  3 | Cost Per KM       | ${COST_PER_KM}")
    print(f"  4 | Insurance Rate    | ${INSURANCE_RATE}")
    print(f"  5 | Rental Discount   | {RENTAL_DISCOUNT}%")
    print(f"  6 | Mileage Discount  | {MILEAGE_DISCOUNT}%")
    print(f"  7 | HST Rate          | {HST_RATE}%")
    print("====================================================")
    # Function to Safely Update a Constant
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

    # Update Constants Based on User Choice
    while True:
        choice = input("\nType number to change, or : ").strip()
        
        if choice == '':
            break
        elif choice == '1':
            COMPANY_NAME = input(f"New Company Name [{COMPANY_NAME}]: ") or COMPANY_NAME
        elif choice == '2':
            DAILY_RENTAL_RATE = update_constant(f"New Daily Rental Rate [${DAILY_RENTAL_RATE}]: ", DAILY_RENTAL_RATE)
        elif choice == '3':
            COST_PER_KM = update_constant(f"New Cost Per KM [${COST_PER_KM}]: ", COST_PER_KM)
        elif choice == '4':
            INSURANCE_RATE = update_constant(f"New Insurance Rate [${INSURANCE_RATE}]: ", INSURANCE_RATE)
        elif choice == '5':
            RENTAL_DISCOUNT = update_constant(f"New Rental Discount [{RENTAL_DISCOUNT}%]: ", RENTAL_DISCOUNT)
        elif choice == '6':
            MILEAGE_DISCOUNT = update_constant(f"New Mileage Discount [{MILEAGE_DISCOUNT}%]: ", MILEAGE_DISCOUNT)
        elif choice == '7':
            HST_RATE = update_constant(f"New HST Rate [{HST_RATE}%]: ", HST_RATE)
        else:
            print("Invalid choice. Please enter a number between 1 and 7, or 'done' to proceed.")

    # Convert Percentages to Decimals for Calculations
    RENTAL_DISCOUNT /= 100
    MILEAGE_DISCOUNT /= 100
    HST_RATE /= 100
# -----------------------
#  User Input and Validation
# -----------------------

# Function to Validate Integer Input
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Collect Customer Details and Rental Information
customer_name  = input("\nCustomer Name       : ").strip()
phone_number   = input("Customer Phone #    : ").strip()
days_rented    = get_valid_int("Day(s) with Rental : ")
odometer_start = get_valid_int("Odometer Start      : ")
odometer_end   = get_valid_int("Odometer End        : ")

# -----------------------
#  Calculations
# -----------------------

# Calculate Total Kilometers Traveled
km_traveled = odometer_end - odometer_start

# Calculate Various Costs
rental_cost    = days_rented * DAILY_RENTAL_RATE
mileage_cost   = km_traveled * COST_PER_KM
insurance_cost = days_rented * INSURANCE_RATE

# Calculate Discounts
rental_discount  = rental_cost * RENTAL_DISCOUNT
mileage_discount = mileage_cost * MILEAGE_DISCOUNT
total_discount   = rental_discount + mileage_discount

# Calculate Total Rental Cost
total_rental_cost = rental_cost + mileage_cost + insurance_cost - total_discount

# Calculate HST
hst = total_rental_cost * HST_RATE

# Calculate Final Invoice Total
final_invoice = total_rental_cost + hst

# -----------------------
#  Display Results
# -----------------------

# Display the Invoice in a Structured Layout
print("\n==================== Invoice ====================")
print(f"Customer            : {customer_name}")
print(f"Phone #             : {phone_number}")
print(f"Odometer (Start/End): {odometer_start} KM / {odometer_end} KM")
print(f"Total KM Traveled   : {km_traveled} KM")
print(f"Rental Period       : {days_rented} day(s)")
print(f"Rental Cost         : ${rental_cost:.2f}")
print(f"Mileage Cost        : ${mileage_cost:.2f}")
print(f"Insurance Cost      : ${insurance_cost:.2f}")
print(f"Total Discount      : -${total_discount:.2f}")
print(f"Sub-Total           : ${total_rental_cost:.2f}")
print(f"HST                 : +${hst:.2f}")
print(f"Final Invoice       : ${final_invoice:.2f}")
print("=================================================")
