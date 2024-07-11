withdraw = 0
user = 0
balance = 0

while user != -1:

	user = int(input('enter 1 to deposit or enter 2 to withdraw or enter 3 to check balance or enter 0 to exit:'))
		
	
	if user == 1:
		deposit = int(input('enter the amount to deposit:'))
		if deposit < 0
			print("invalid") 
		balance += deposit

	elif user == 2:
		withdraw = int(input('enter the amount to withdraw:'))
		if withdraw > balance:
			print("invalid")
		else:
			balance -= withdraw
		

	elif user == 3:
		print(balance)
	


	elif user == 0:
		break

	else:
		break

