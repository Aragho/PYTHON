first_integer = int(input('enter a integers:'))
second_integer = int(input('enter a integers:'))
third_integer = int(input('enter a integers:'))

sum = first_integer + second_integer + third_integer
average = sum / 3
product = first_integer * second_integer * third_integer

print('Sum is ',sum)
print('Average is',average)
print('Product is',product)

if first_integer > second_integer and first_integer > third_integer:
	print('Largest number is ', first_integer)

elif second_integer > first_integer and second_integer > third_integer:
	print('Largest number is ', second_integer)

elif third_integer > first_integer and third_integer > second_integer:
	print('Largest number is ', third_integer)

if first_integer < second_integer and first_integer < third_integer:
	print('Smallest number is ', first_integer)

elif second_integer < first_integer and second_integer < third_integer:
	print(' Smallest number is ', second_integer)

elif third_integer < first_integer and third_integer < second_integer:
	print('Smallest number is ', third_integer)






