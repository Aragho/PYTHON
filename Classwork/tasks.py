def len_numbers(numbers):
	result = 0
	for alphabet in numbers:
		result += 1
	return result

user_input = input('Enter  number: ')
result = len_numbers(user_input)
print(result)
	