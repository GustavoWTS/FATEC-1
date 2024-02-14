# Do an algorithm that reads salary and the percentage of the raise, then calculate and show the new salary accordingly the percentage typed by the user.
salary = float(input('Type the salary: '))
percentage_raise = float(input('Type the percentage raise: '))
salary_adjustment = salary * percentage_raise
new_salary = salary + salary_adjustment
print('The new salary after the adjustment is:', new_salary)

