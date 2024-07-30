def even_and_odd(number):
	for index in range(len(number)):
		if index % 2 == 0:
			return number[index]
		elif index % 2 != 0:
			return number[index]

integers = input('Enter a number:')
result = even_and_odd(integers)
print(f'number,{even number}')

			













def odd_position(number):
	
	for index in range (len(number)):
		if index % 2 != 0:
			print(number[index])
	return number[index]

odd = [2, 20, 30, 40, 50, 60, 70, 80]
position = odd_position(odd)
print(position)