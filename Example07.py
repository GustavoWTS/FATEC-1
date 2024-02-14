#The FrangoTech farm has automated control of every chicken in its production. 
# On the chicken's right foot there is a ring with an identification chip. 
# In the left foot there are two rings to indicate the type of food food it should consume. 
# Knowing that the ring with the chip costs 04.00 BRL and the food ring costs 03.50 BRL each, draw up a flowchart to calculate and show the farm's total expenditure to tag all its chickens.

chip_cost = 4.00
food_ring_cost = 3.50
num_chickens = int(input("Enter the number of chickens: "))
total_chip_cost = num_chickens * chip_cost
total_food_ring_cost = num_chickens * 2 * food_ring_cost  # Two rings per chicken
total_expenditure = total_chip_cost + total_food_ring_cost
print("Total expenditure to tag all chickens:", total_expenditure, "BRL")
