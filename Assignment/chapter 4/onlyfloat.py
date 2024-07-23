def only_float(a, b):
 
	if type (a) == float and type (b) == float:
		return 2

	elif type (a) == float and type (b)!= float:
		return 1

	else:
		return 0
user1 = (input('Enter first number: '))
user2 = (input('Enter second number: '))
result = only_float(user1, user2)

print (result)