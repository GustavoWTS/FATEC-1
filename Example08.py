#It is known that 1 foot is equal to 12 inches, 1 yard is equal to 3 feet and 1 mile is equal to 1760 yards. is equal to 1760 yards. Create an algorithm in Python that reads a measurement in feet, perform the following conversions and display the results in: (a) inches; (b) yards; (c) miles.

feet = float(input("Enter the measurement in feet: "))
inches = feet * 12
yards = feet / 3
miles = yards / 1760
print("Measurement in inches:", inches)
print("Measurement in yards:", yards)
print("Measurement in miles:", miles)
