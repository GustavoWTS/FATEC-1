#In one state, DETRAN charges a 1% fee for vehicle transfers CHARGES A 1% FEE FOR CARS MANUFACTURED BEFORE 1990
# AND A CHARGE OF 1.5% for those manufactured from 1990 onwards, a charge that on the value of the car. 
# The program reads the year and price of the car and then then calculates and prints out the tax to be paid.
# Read the year and price of the car from the user
year = int(input("Enter the year of manufacture of the car: "))
price = float(input("Enter the price of the car: "))

if year < 1990:
    tax_rate = 0.01
else:
    tax_rate = 0.015

tax = price * tax_rate
print("Tax to be paid:", tax)
