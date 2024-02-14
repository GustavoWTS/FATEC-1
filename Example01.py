# Do an algorithm that reads two values, calculated and show the division math between them.
value1 = float(input('Type the first value: '))
value2 = float(input('Type the second value: '))
if value2 == 0:
    print('Error! Division by zero is not allowed')
else:
    result = value1 / value2
    print('The result of the division is:', result)
