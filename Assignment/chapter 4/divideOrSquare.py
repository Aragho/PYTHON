def divide_or_square(number):
	if number % 5 == 0:
		return number**0.5

	elif number % 5 != 0:
		return number % 5

user_input = int(input('Enter a number: '))
result = divide_or_square(user_input)

print(result)












	 