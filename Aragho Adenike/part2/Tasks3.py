def even_and_odd():
	even = number % 2 == 0
	odd = number % 3 == 0
	if number % 2 == 0:
		return even
	else:
		return odd

number = int(input('Enter a number:'))
print(even_and_odd())