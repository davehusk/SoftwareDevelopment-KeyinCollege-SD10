'''
Honest Harry Car Sales Program
Developed by: Dave Husk dave.husk@keyin.com
V 0.9b
Date: 2023-10-19

Note: Instructions specify to use HST, therefore assumed prov is NL
'''

# Import
import datetime

# Constants
HST_RATE = 0.15
LICENSE_FEE_LOW = 75.00
LICENSE_FEE_HIGH = 165.00
TRANSFER_FEE_RATE = 0.01
LUXURY_TAX_RATE = 0.016
FINANCING_FEE = 39.99

# Main Input Loop
while True:
      print()  
      first_name = input("Enter customer's first name, or 'END' to quit: ").upper()
      
      # Check to exit
      if first_name == 'END':
            print()
            break
      last_name = input("Enter customer's last name: ").title()
      
      # Check phone number
      while True:
            phone_number = input("Enter the 10-digit phone number: ")
            if len(phone_number) == 10:
                  break
            print("Invalid phone number. Use 10 digits (7091234567)")
            
      # Check plate
      while True:
            plate_number = input("Enter the 6-character plate number: ")
            if len(plate_number) == 6:
                  plate_number = plate_number.upper()
                  break
            print("Invalid plate number. Use: ABC123")
      # Gather rest of inputs
      car_make = input("Enter car make:  ").title()
      car_model = input("Enter car model: ").title()
      car_year = input("Enter car year:  ")
      salesperson_name = input("Enter the salesperson's name: ").title()
      selling_price = float(input("Enter selling price: "))
      trade_in = float(input("Enter trade-in value: "))
      
      # Testing #'s
      car_make = "Chevy"
      car_model = "Honda"
      car_year = "1900"
      salesperson_name = "Billy Bob"
      selling_price = float("20000.00")
      trade_in = float("15000.00")

      # Calculations
      price_after_trade = selling_price - trade_in
      if price_after_trade <= 5000.00:
            license_fee = LICENSE_FEE_LOW
      else:
            license_fee = LICENSE_FEE_HIGH

      transfer_fee = selling_price * TRANSFER_FEE_RATE
      # Check value
      if selling_price > 20000:
            transfer_fee += selling_price * LUXURY_TAX_RATE
      # Math
      subtotal = price_after_trade + license_fee + transfer_fee
      hst = subtotal * HST_RATE
      total_price = subtotal + hst

      # Generate Receipt ID
      customer_initials = first_name[0] + last_name[0]
      receipt_id = f"{customer_initials.upper()}-{plate_number[-3:]}-{phone_number[-4:]}"

      # Date Formatting
      current_date = datetime.datetime.now().strftime("%B %d, %Y")
      first_payment_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%d-%b-%y").upper()

      # Text in output
      cust_rec = first_name[0] + ". " + last_name

      # Output RECEIPT
      print()
      print('123456789012345678901234567890123456789012345678901234567890123456789012345678')
      print("------------------------------------------------------------------------------")
      print()
      print(f" Honest Harry Car Sales                    Invoice Date:     {current_date}")
      print(f" Used Car Sale and Receipt                 Receipt No:            {receipt_id}")
      print()
      print(f"                                           Sale Price:             $ {selling_price:.2f}")
      print(f" Sold to:          Sold by: {salesperson_name:<14} Trade Allowance:        $ {trade_in:.2f}")
      print("                                           ----------------------------------")
      print(f"      {cust_rec:<29}        Price After Trade:      ${price_after_trade:>9.2f}")
      print(f"      1234 David's Awesome Way             License Fee:            ${license_fee:>9.2f}")
      print(f"      Came-by-chance, NL A0A1A1            Transfer Fee:           ${transfer_fee:>9.2f}")
      print("                                           ----------------------------------")
      print(f" Car Details:                              Subtotal:               ${subtotal:>9.2f}")
      print(f"                                           15% HST:                ${hst:>9.2f}")
      print(f"      {car_year:>4} {car_make} {car_model:<25} ----------------------------------")
      print(f"                                           Total Sales Price:      ${total_price:>9}")
      print("------------------------------------------------------------------------------")
      print()
      print("                                    Financing      Total        Monthly")
      print('     # Years        # Payments         Fee         Price        Payment')
      print('     ------------------------------------------------------------------')
      
        # Date Formatting
      current_date = datetime.datetime.now().strftime("%B %d, %Y")
      first_payment_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%d-%b-%y").upper()

      # Text in output
      cust_rec = first_name[0].upper() + ". " + last_name

      # Payment Schedule inside receipt
      for years in range(1, 5):
            monthly_payments = years * 12
            financing_fee = years * FINANCING_FEE
            total_with_finance = total_price + financing_fee
            monthly_payment = total_with_finance / monthly_payments
            first_payment_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')
            today_date = (datetime.datetime.now()).strftime('%Y-%m-%d')

            print(f"         {years:<13} {monthly_payments:<10} $ {financing_fee:>6.2f}      $ {total_with_finance:>8,.2f}    $ {monthly_payment:>7,.2f}")

      # Finish receipt
      print("     ------------------------------------------------------------------")
      print(f"     Invoice date: {today_date}            First payment date: {first_payment_date}")
      print()
      print("------------------------------------------------------------------------------")
      print(" " * 20 + "Best used cars at the best prices!")
      print()
      print("END OF RECEIPT")
      print()
      
      # Run script again
      cont = input(" ^---- Would you like to process another sale? (y/n): ").upper()
      print()
      if cont != 'Y':
            break
