number = int(input('enter five-digits integers: '))

first_number = number // 10000
second_number = (number // 1000) % 10
fifth_number = number % 10
fourth_number = ((number %  100) - fifth_number) // 10
	
if first_number == fifth_number and second_number == fourth_number:
	print("Is a palindromes")
else:
	print("Is not a palindromes")



