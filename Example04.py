#Do an algorithm that reads a salary value, calculates a raise of 15% and shows the new salary amount.
salary = float(input('Type the salary value:'))
salary_raise = salary * 0.15
new_salary = salary + salary_raise
print('The new salary after the  raise is:', new_salary)