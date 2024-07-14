passes = 0
failure = 0

for num in range(10):

	user_input = int(input("Enter 1 for pass or 2 for fail: "))

	while user_input != 1 and user_input != 2:
		print("Ya mad")
		user_input = int(input("Enter 1 for pass or 2 for fail: "))

	if user_input == 1:
		passes += 1
	else: 
		failure += 1


print("number of passes is ", passes)
print("number of failure is ", failure)