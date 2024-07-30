def reverse(number):
	integer1 = number % 10
	integer2 = number // 10
	integer3 = number % 10
	integer4 = number // 10
	result = str(integer1) + str(integer2) + str (integer3) + (integer4)
	return result




def is_palindrome(number):
	integer1 = number % 10
	integer2 = number // 10
	integer3 = number % 10
	integer4 = number // 10
	
	if integer4 == integer1:
		result = "true"
	if integer4  != integer1:

		result = "false"
	return result

print(reverse(656))
print(is_palindrome)

	




 

