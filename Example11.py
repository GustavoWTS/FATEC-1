#Build a Python code that reads the amount of money in a company's a company's cashier (CASH), the quantity of products to be purchased (QUANTITY) (QUANTITY) and the price of each unit (PR). If the total value of the is more than 80% of the amount in cash, the purchase must be made on with 10% interest on the total amount. Otherwise, the the customer will receive a 5% discount. It shows the payment method chosen and the amount to be paid ('Cash' or 'Forward') depending on the quantity.


CAIXA = float(input("Enter the amount of money in the cash register: "))
QUANTIDADE = int(input("Enter the quantity of products to be purchased: "))
PR = float(input("Enter the price of each unit: "))


total_cost = QUANTIDADE * PR


if total_cost > 0.8 * CAIXA:
    
    forma_pagamento = "A prazo"
    valor_pago = total_cost * 1.10
else:
 
    forma_pagamento = "A vista"
    valor_pago = total_cost * 0.95


print("Forma de pagamento:", forma_pagamento)
print("Valor a ser pago:", valor_pago)
