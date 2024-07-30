def reverse(number):
	integer1 = number % 10
	integer2 = number // 10
	result = str(integer1) + str(integer2)
	return result




def is_palindrome(number):
	integer1 = number % 10
	integer2 = number // 10
	
		
	if integer2 == integer1:
		result = "true"
	if integer2  != integer1:
		result = "false"
	return result

	



print(reverse(456))
print(is_palindrome)



 

