def square(number):
		"""calculate and return 
		the square of its argument 
		parameter: an int, float
		"""
		return number ** 2

print(square(10))



def do_stuff(number,list_of_numbers):
	for num in list_of_numbers:
		number += num
	return number

print(do_stuff(10, [1, 2, 3, 4, 5]))
print(do_stuff(list_of_numbers=[1, 2, 3, 4, 5], number=(10)))



def get_product(*numbers):
	product = 1
	for number in numbers:
		product *= number

	return product

print(get_product(1, 4, 5))
print(get_product(2, 4, 8, 10))
print(get_product(5, 8))
print(get_product(2, 2, 2, 2, 2, 2, 2, 2, 2, 2))


