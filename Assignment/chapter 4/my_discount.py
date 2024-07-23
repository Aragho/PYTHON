def my_discount(price, discount):
	
	product = price * discount / 100
	new_product = price - product
	return new_product


user_input1 = int(input('Enter first number:'))
user_input2 = int(input('Enter second number:'))
result = my_discount(user_input1, user_input2)

print(result)	