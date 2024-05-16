"""
======================================================================================
   St. John's Marina & Yacht Club Administrative System - Version: 1.0alpha
      Author: David Husk Jr - Email: dave.husk@keyin.com
______________________________________________________________________________________


Program Description
This Python-based script serves as the digital backbone for the 
St. John's Marina & Yacht Club's administrative operations. It empowers 
the receptionist and club administrators to efficiently manage yacht docking 
records, billing, and membership management. 

Key Features
- Entry of existing club members and addition of new members.
- Tracking of yacht docking information, including member details and payment status.
- Generation of receipts for financial transactions.
- Optimized site allocation for members, ensuring efficient utilization.
- User-friendly interface for seamless navigation.
- Data security and integrity to safeguard sensitive information.

Usage Guidelines
- The system is intended for use by the administrative staff of St. John's Marina & Yacht Club. 
- Proper training and guidelines are provided to ensure effective utilization.

Support
- Contact via email dave.husk@keyin.com
"""

# Import
import datetime
import time
import os

# Initialize Constants
TAX_RATE = 0.15
STANDARD_DUES = 75.00
EXECUTIVE_DUES = 150.00
PROCESSING_FEE = 59.99

# Function to simulate typing animation
def typing_animation(text, speed):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()  # Newline at the end

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Displaying Animated ASCII Art or Text
typing_animation("_____________________________________________________", 0.01)
typing_animation(" St. John's Marina & Yacht Club Administrative System", 0.015)
typing_animation("- Version: 1.0alpha", 0.005)
typing_animation("_____________________________________________________", 0.01)
print()
time.sleep(0.5)

# Collect input from user
site_number =    int(input("Enter the site number (1-100):              "))
num_alternates = int(input("Enter the number of alternate members:      "))
print("Enter the membership type ")
membership_type =    input("         (S for Standard, E for Executive): ").upper()
cleaning =           input("Weekly site cleaning (Y for Yes, N for No): ").upper()
surveillance =       input("Video surveillance (Y for Yes, N for No):   ").upper()
time.sleep(1)
print()
member_name =        input("Enter the member's name:                    ").capitalize()
address =            input("Enter the street address:                   ").upper()
city =               input("Enter the city:                             ").upper()
province = "NL"
# province =         input("Enter the province:                         ").upper()
postal_code =        input("Enter the postal code (A1A1A1):             ").upper()
phone_number =       input("Enter the phone number (709xxxxxxx):        ")
cell_number =        input("Enter the cell number (709xxxxxxx):         ")
print()
time.sleep(0.5)


# Define a function to calculate the monthly and yearly charges
def calculate_charges(site_number, num_alternates, cleaning, surveillance, membership_type):
    # Determine site charge based on site number
    if site_number % 2 == 0:
        site_charge = 80.00
    else:
        site_charge = 120.00
    
    # Calculate alternate member charge
    alternate_charge = 5.00 * num_alternates
    
    # Calculate extra charges for cleaning and surveillance
    cleaning_charge = 50.00 if cleaning == 'Y' else 0.00
    surveillance_charge = 35.00 if surveillance == 'Y' else 0.00
    
    # Calculate subtotal, taxes, and total monthly charges
    subtotal = site_charge + alternate_charge + cleaning_charge + surveillance_charge
    taxes = subtotal * TAX_RATE
    total_monthly = subtotal + taxes
    yearly_site = subtotal * 12
    yearly_taxes = taxes * 12
    
    # Add monthly dues based on membership type
    monthly_dues = STANDARD_DUES if membership_type == 'S' else EXECUTIVE_DUES
    total_monthly += monthly_dues
    
    # Calculate yearly fees and monthly payment
    total_yearly = total_monthly * 12
    monthly_payment = (total_yearly + PROCESSING_FEE) / 12
    
    # Calculate cancellation fee
    cancellation_fee = 0.6 * (site_charge * 12)

    # Add yearly extra charges and yearly subtotal
    yearly_cleaning_charge = cleaning_charge * 12
    yearly_surveillance_charge = surveillance_charge * 12
    yearly_extras = yearly_cleaning_charge + yearly_surveillance_charge
    yearly_subtotal = yearly_site + yearly_extras + yearly_taxes
        
    return total_monthly, total_yearly, monthly_payment, cancellation_fee, yearly_site, yearly_taxes, yearly_extras, yearly_subtotal, monthly_dues
          
# Calculate all the required fees
total_monthly, total_yearly, monthly_payment, cancellation_fee, yearly_site, yearly_taxes, yearly_extras, yearly_subtotal, monthly_dues = calculate_charges(site_number, num_alternates, cleaning, surveillance, membership_type)

# Display the invoice
print(f" ________________________________________")
print(f"|    St. John's Marina and Yacht Club    |")
print(f"|         Yearly Member Receipt          |")
print(f"|________________________________________|")
print(f"|                                        |")
print(f"|Client Name and Address:                |")
print(f"|                                        |")
print(f"| {member_name:<39}|")
print(f"| {address:<39}|")
print(f"| {city:<20} {province:<2} {postal_code}         |")
print(f"|                                        |")
print(f"| Phone: {phone_number:<10} (H)                  |")
print(f"|        {cell_number:<10} (C)                  |")
print(f"|                                        |")
print(f"|  Site #: {site_number}      Member Type: {'Standard' if membership_type == 'S' else 'Executive'}  |")
print(f"|                                        |")
print(f"|Alternate Members:                  {num_alternates:>4}|")
print(f"|Weekly Site Cleaning:                {'Yes' if cleaning == 'Y' else 'No'}|")
print(f"|Video Surveillance:                  {'Yes' if surveillance == 'Y' else 'No'}|")
print(f"|                                        |")
print(f"|Site Charges:                ${yearly_site: >10,.2f}|")
print(f"|Extra Charges:               ${yearly_extras: >10,.2f}|")
print(f"|                             -----------|")
print(f"|Subtotal:                    ${yearly_subtotal: >10,.2f}|")
print(f"|Sales Tax (HST):             ${yearly_taxes: >10,.2f}|")
print(f"|                             -----------|")
print(f"|Total Monthly Charges:       ${total_monthly: >10,.2f}|")
print(f"|Monthly Dues:                ${monthly_dues: >10,.2f}|")
print(f"|                             ___________|")
print(f"|Total Monthly Fees:          ${total_monthly: >10,.2f}|")
print(f"|Total Yearly Fees:           ${total_yearly: >10,.2f}|")
print(f"|                             ===========|")
print(f"|Monthly Payment:             ${monthly_payment:>10,.2f}|")
print(f"|________________________________________|")
print(f"|                                        |")
print(f"|Issued:    {datetime.datetime.now().strftime('%Y-%m-%d'): <29}|")
print(f"|HST Reg #: 549-33-5849-4720-9885        |")
print(f"|                                        |")
print(f"|Cancellation Fee:            ${cancellation_fee:>10,.2f}|")
print(f"|________________________________________|")