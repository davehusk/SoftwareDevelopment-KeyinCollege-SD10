import datetime
import re
import matplotlib.pyplot as plt
import json

# Default values
next_policy_number = 1944
basic_premium = 869.00
discount_for_additional_cars = 0.25
cost_of_extra_liability_coverage = 130.00
cost_of_glass_coverage = 86.00
cost_for_loaner_car_coverage = 58.00
hst_rate = 0.15
processing_fee = 39.99

# Lists to store previous claims and customer data
claim_dates = []
claim_amounts = []
customer_data = []

# Function to validate province
def validate_province(province):
    provinces = ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "PE", "NL"]
    return province.upper() in provinces

# Function to validate postal code format
def validate_postal_code(postal_code):
    pattern = r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$'
    return bool(re.match(pattern, postal_code))

# Function to validate phone number format
def validate_phone_number(phone_number):
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, phone_number))

# Function to calculate insurance premium
def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    try:
        num_cars = int(num_cars)
    except ValueError:
        raise ValueError("Number of cars must be a valid integer.")
    
    if num_cars < 1:
        raise ValueError("Number of cars must be at least 1.")
    
    extra_liability = extra_liability.upper()
    glass_coverage = glass_coverage.upper()
    loaner_car = loaner_car.upper()

    # Calculate extra costs
    extra_costs = (num_cars - 1) * basic_premium * discount_for_additional_cars
    if extra_liability == 'Y':
        extra_costs += num_cars * cost_of_extra_liability_coverage
    if glass_coverage == 'Y':
        extra_costs += num_cars * cost_of_glass_coverage
    if loaner_car == 'Y':
        extra_costs += num_cars * cost_for_loaner_car_coverage

    # Calculate total insurance premium
    total_premium = basic_premium + extra_costs

    # Calculate HST
    hst = total_premium * hst_rate

    # Calculate total cost
    total_cost = total_premium + hst

    return total_cost

# Function to calculate monthly payment
def calculate_monthly_payment(total_cost, payment_method, down_payment=0):
    if payment_method == 'Full':
        return total_cost
    elif payment_method == 'Monthly':
        return (total_cost + processing_fee) / 8
    elif payment_method == 'Down Pay':
        remaining_cost = total_cost - down_payment
        return (remaining_cost + processing_fee) / 8

# Function to display receipt
def display_receipt(first_name, last_name, address, city, province, postal_code, phone_number,
                    num_cars, extra_liability, glass_coverage, loaner_car, payment_method, down_payment):
    # Convert to title case and uppercase
    first_name = first_name.title()
    last_name = last_name.title()
    city = city.title()
    province = province.upper()
    extra_liability = extra_liability.upper()
    glass_coverage = glass_coverage.upper()
    loaner_car = loaner_car.upper()

    # Calculate insurance premium
    total_cost = calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car)

    # Calculate monthly payment
    monthly_payment = calculate_monthly_payment(total_cost, payment_method, down_payment)


    # Display receipt
    print("One Stop Insurance Company - Receipt")
    print("=====================================")
    print(f"Policy Number: {next_policy_number}")
    print(f"Customer: {first_name} {last_name}")
    print(f"Address: {address}, {city}, {province}, {postal_code}")
    print(f"Phone Number: {phone_number}")
    print(f"Number of Cars: {num_cars}")
    print(f"Extra Liability Coverage: {extra_liability}")
    print(f"Glass Coverage: {glass_coverage}")
    print(f"Loaner Car Coverage: {loaner_car}")
    print(f"Payment Method: {payment_method}")
    if payment_method == 'Down Pay':
        print(f"Down Payment: ${down_payment:.2f}")
    print(f"Insurance Premium: ${total_cost:.2f}")
    print(f"HST (15%): ${total_cost * hst_rate:.2f}")
    print(f"Total Cost: ${total_cost + total_cost * hst_rate:.2f}")
    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print("=====================================")
    print("Previous Claims:")
    print("Claim #   Claim Date   Amount")
    print("---------------------------------")
    for i in range(len(claim_dates)):
        print(f"{i + 1}. {claim_dates[i]} ${claim_amounts[i]:,.2f}")

# Function to gather customer information
def gather_customer_information():
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")
    address = input("Enter customer's address: ")
    city = input("Enter customer's city: ")
    province = input("Enter customer's province (e.g., ON, QC, BC): ")
    while not validate_province(province):
        province = input("Invalid province. Please enter a valid province: ")
    postal_code = input("Enter customer's postal code: ")
    while not validate_postal_code(postal_code):
        postal_code = input("Invalid postal code. Please enter a valid postal code: ")
    phone_number = input("Enter customer's phone number: ")
    while not validate_phone_number(phone_number):
        phone_number = input("Invalid phone number. Please enter a valid 10-digit phone number: ")
    num_cars = input("Enter the number of cars being insured: ")
    extra_liability = input("Extra Liability Coverage (Y/N): ")
    glass_coverage = input("Glass Coverage (Y/N): ")
    loaner_car = input("Loaner Car Coverage (Y/N): ")
    payment_method = input("Payment Method (Full/Monthly/Down Pay): ")

    if payment_method == 'Down Pay':
        down_payment = input("Enter the amount of the down payment: ")
    else:
        down_payment = '0'

    # Gather previous claims information
    print("Enter previous claims information. Press Enter to finish.")
    while True:
        claim_date = input("Claim Date (YYYY-MM-DD): ")
        if not claim_date:
            break
        claim_amount = input("Claim Amount: $")
        claim_dates.append(claim_date)
        claim_amounts.append(claim_amount)

    # Store customer data
    customer_data.append({
        "First Name": first_name,
        "Last Name": last_name,
        "Address": address,
        "City": city,
        "Province": province,
        "Postal Code": postal_code,
        "Phone Number": phone_number,
        "Number of Cars": num_cars,
        "Extra Liability Coverage": extra_liability,
        "Glass Coverage": glass_coverage,
        "Loaner Car Coverage": loaner_car,
        "Payment Method": payment_method,
        "Down Payment": down_payment,
        "Claims": [{"Claim Date": date, "Claim Amount": amount} for date, amount in zip(claim_dates, claim_amounts)]
    })

    return (first_name, last_name, address, city, province, postal_code, phone_number,
            num_cars, extra_liability, glass_coverage, loaner_car, payment_method, down_payment)

# Function to save customer data to a JSON file
def save_customer_data():
    with open("customer_data.json", "w") as json_file:
        json.dump(customer_data, json_file, indent=4)

# Function to load customer data from a JSON file
def load_customer_data():
    try:
        with open("customer_data.json", "r") as json_file:
            data = json.load(json_file)
            customer_data.extend(data)
    except FileNotFoundError:
        pass

# Function to navigate the program
def main():
    load_customer_data()  # Load existing customer data
    while True:
        print("One Stop Insurance Company - Policy Management")
        print("=============================================")
        print("1. Enter Customer Information")
        print("2. Generate Receipt")
        print("3. Generate Sales Graph")
        print("4. Exit")
        
        choice = input("Select an option (1/2/3/4): ")
        
        if choice == '1':
            customer_info = gather_customer_information()
            save_customer_data()  # Save customer data after each entry
        elif choice == '2':
            if not customer_data:
                print("No customer information available. Please enter customer data first.")
            else:
                display_receipt(*customer_info)
        elif choice == '3':
            generate_sales_graph()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

# Function to generate a sales graph
def generate_sales_graph():
    # Define monthly sales data (you can replace these values with your own)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales = [25000, 28000, 32000, 31000, 35000, 38000, 41000, 39000, 43000, 46000, 49000, 52000]

    # Create a bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(months, sales, color='skyblue')
    plt.xlabel("Months")
    plt.ylabel("Total Sales ($)")
    plt.title("Total Sales by Month")

    # Add data labels to the bars
    for i, sale in enumerate(sales):
        plt.text(i, sale + 500, f"${sale:,.0f}", ha='center', va='bottom')

    # Show the graph
    plt.tight_layout()
    plt.show()

# Entry point of the program
if __name__ == "__main__":
    main()
