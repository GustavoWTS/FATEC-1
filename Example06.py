# Do an algorithm that receives the price of a product, calculates and shows the new price knowing that this price suffered an discount of ten percent.
product_price = float(input('Enter the price of the product: '))
discount = product_price * 0.10
new_price = product_price - discount
print('The new price after a 10% discount is:', new_price)
