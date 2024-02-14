#John bought a computer to keep track of his daily work output. Every time he brings in more fish than the weight established by the state of São Paulo's fishing regulations (50KG), he has to pay a fine of R$4.00 per excess KG. João needs you to make a flowchart that takes the variable P (weight of fish) and checks if there is an excess. If there is, record in variable E (excess) and in variable M (the amount of the fine) that must be paid. If not, reset the variables to zero and show whether or not the excess and fine have been paid.

P = float(input("Enter the weight of fish (in KG): "))

if P > 50:
    E = P - 50
    M = 4 * E
    print(f"Excess weight: {E} KG")
    print(f"Fine amount: R${M}")
else:
    E = 0
    M = 0
    print("No excess or fine.")

