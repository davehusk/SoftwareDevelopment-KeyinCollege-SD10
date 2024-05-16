# Importing Required Libraries
from datetime import datetime

# Constants for Basic Customization
SITE_COST_EVEN = 80  # Monthly cost for even-numbered sites
SITE_COST_ODD = 120  # Monthly cost for odd-numbered sites
ALT_MEMBER_COST = 5  # Monthly cost for each alternate member
CLEANING_COST = 50   # Monthly cost for weekly site cleaning
SURVEILLANCE_COST = 35 # Monthly cost for video surveillance
STANDARD_DUES = 75   # Monthly dues for Standard members
EXECUTIVE_DUES = 150 # Monthly dues for Executive members
TAX_RATE = 0.15      # Tax rate (15%)
PROCESSING_FEE = 59.99 # Processing fee for yearly payment
CANCEL_FEE_RATE = 0.6 # Cancellation fee as a rate of yearly site charges

# Marina Member Class
class MarinaMember:
    def __init__(self, site_num, name, address, city, province, postal, phone, cell, member_type, alt_count, weekly_cleaning, surveillance):
        self.site_num = site_num
        self.name = name
        self.address = address
        self.city = city
        self.province = province
        self.postal = postal
        self.phone = phone
        self.cell = cell
        self.member_type = "Standard" if member_type == "S" else "Executive"
        self.alt_count = alt_count
        self.weekly_cleaning = weekly_cleaning == "Y"
        self.surveillance = surveillance == "Y"
        
        # Financial calculations
        self.site_charge = SITE_COST_EVEN if site_num % 2 == 0 else SITE_COST_ODD
        self.extra_charge = (CLEANING_COST if self.weekly_cleaning else 0) + (SURVEILLANCE_COST if self.surveillance else 0) + (ALT_MEMBER_COST * self.alt_count)
        self.subtotal = self.site_charge + self.extra_charge
        self.tax = self.subtotal * TAX_RATE
        self.total_monthly = self.subtotal + self.tax + (STANDARD_DUES if member_type == "S" else EXECUTIVE_DUES)
        self.total_yearly = self.total_monthly * 12
        self.monthly_payment = (self.total_yearly + PROCESSING_FEE) / 12
        self.cancel_fee = self.site_charge * 12 * CANCEL_FEE_RATE

# Main Function
def main():
    # Data storage for marina members
    members = {}
    
    while True:
        print("\nMarina Club Member Management")
        print("1. Add Member")
        print("2. Generate Receipt")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Collect input and create a MarinaMember object
            site_num = int(input("Enter the Site Number (1-100): "))
            name = input("Enter the member name: ")
            address = input("Enter the address: ")
            city = input("Enter the city: ")
            province = input("Enter the province: ")
            postal = input("Enter the postal code: ")
            phone = input("Enter the phone number: ")
            cell = input("Enter the cell number: ")
            member_type = input("Enter the membership type (S/E): ")
            alt_count = int(input("Enter the number of alternate members: "))
            weekly_cleaning = input("Weekly site cleaning (Y/N): ")
            surveillance = input("Video surveillance (Y/N): ")
            
            member = MarinaMember(site_num, name, address, city, province, postal, phone, cell, member_type, alt_count, weekly_cleaning, surveillance)
            members[site_num] = member
            
        elif choice == 2:
            site_num = int(input("Enter the Site Number for the receipt: "))
            member = members.get(site_num)
            if member:
                print(f"Receipt for {member.name} (Site: {member.site_num})")
                print(f"Address: {member.address}, {member.city}, {member.province}, {member.postal}")
                print(f"Phone: {member.phone}, Cell: {member.cell}")
                print(f"Membership Type: {member.member_type}")
                print(f"Weekly Cleaning: {'Yes' if member.weekly_cleaning else 'No'}, Surveillance: {'Yes' if member.surveillance else 'No'}")
                print(f"Total Monthly Fees: ${member.total_monthly:.2f}")
                print(f"Total Yearly Fees: ${member.total_yearly:.2f}")
                print(f"Monthly Payment: ${member.monthly_payment:.2f}")
                print(f"Cancellation Fee: ${member.cancel_fee:.2f}")
                
        elif choice == 3:
            print("Exiting the program.")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Marina Member Class
class MarinaMember:
    def __init__(self, site_num, name, address, city, province, postal, phone, cell, member_type, alt_count, weekly_cleaning, surveillance):
        self.site_num = site_num
        self.name = name
        self.address = address
        self.city = city
        self.province = province
        self.postal = postal
        self.phone = phone
        self.cell = cell
        self.member_type = "Standard" if member_type == "S" else "Executive"
        self.alt_count = alt_count
        self.weekly_cleaning = weekly_cleaning == "Y"
        self.surveillance = surveillance == "Y"
        
        # Financial calculations
        self.site_charge = SITE_COST_EVEN if site_num % 2 == 0 else SITE_COST_ODD
        self.extra_charge = (CLEANING_COST if self.weekly_cleaning else 0) + (SURVEILLANCE_COST if self.surveillance else 0) + (ALT_MEMBER_COST * self.alt_count)
        self.subtotal = self.site_charge + self.extra_charge
        self.tax = self.subtotal * TAX_RATE
        self.total_monthly = self.subtotal + self.tax + (STANDARD_DUES if member_type == "S" else EXECUTIVE_DUES)
        self.total_yearly = self.total_monthly * 12
        self.monthly_payment = (self.total_yearly + PROCESSING_FEE) / 12
        self.cancel_fee = self.site_charge * 12 * CANCEL_FEE_RATE

# Function to List Members
def list_members(members):
    if not members:
        print("\nNo members are currently in the list.")
    else:
        print("\nList of Members:")
        for site_num, member in members.items():
            print(f"Site Number: {site_num}, Name: {member.name}, Membership Type: {member.member_type}")


# Function to Delete a Member
def delete_member(members):
    site_num = int(input("Enter the Site Number of the member to delete: "))
    if site_num in members:
        del members[site_num]
        print(f"Member at Site Number {site_num} has been deleted.")
    else:
        print(f"No member found at Site Number {site_num}.")

# Main Function
def main():
    # Data storage for marina members
    members = {}
    
    while True:
        print("\nSt. John’s Marina & Yacht Club")
        print()
        print("1. Add Member")
        print("2. Generate Receipt")
        print("3. List Members")
        print("4. Delete Member")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Collect input and create a MarinaMember object
            site_num = int(input("Enter the Site Number (1-100): "))
            name = input("Enter the member name: ")
            address = input("Enter the address: ")
            city = input("Enter the city: ")
            province = input("Enter the province: ")
            postal = input("Enter the postal code: ")
            phone = input("Enter the phone number: ")
            cell = input("Enter the cell number: ")
            member_type = input("Enter the membership type (S/E): ")
            alt_count = int(input("Enter the number of alternate members: "))
            weekly_cleaning = input("Weekly site cleaning (Y/N): ")
            surveillance = input("Video surveillance (Y/N): ")
            
            member = MarinaMember(site_num, name, address, city, province, postal, phone, cell, member_type, alt_count, weekly_cleaning, surveillance)
            members[site_num] = member
            
            print('Saved Site #:', site_num)
            
        elif choice == 2:
            # Generate and print the receipt for a member
            site_num = int(input("Enter the Site Number for the receipt: "))
            member = members.get(site_num)
            if not members:
              print("\nNo members are currently in the list.")
            else:
                print(f"Receipt for {member.name} (Site: {member.site_num})")
                print(f"Address: {member.address}, {member.city}, {member.province}, {member.postal}")
                print(f"Phone: {member.phone}, Cell: {member.cell}")
                print(f"Membership Type: {member.member_type}")
                print(f"Weekly Cleaning: {'Yes' if member.weekly_cleaning else 'No'}, Surveillance: {'Yes' if member.surveillance else 'No'}")
                print(f"Total Monthly Fees: ${member.total_monthly:.2f}")
                print(f"Total Yearly Fees: ${member.total_yearly:.2f}")
                print(f"Monthly Payment: ${member.monthly_payment:.2f}")
                print(f"Cancellation Fee: ${member.cancel_fee:.2f}")
                
        elif choice == 3:
            list_members(members)

        elif choice == 4:
            delete_member(members)

        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Uncomment to run the program
main()
