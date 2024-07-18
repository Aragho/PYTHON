from random import randint

guess = randint(1, 1001)

print(guess)
print("Welcome to the Number guessing game!")

start_game = input("Enter yes to start or no to stop playing:")
while start_game.lower() != "yes" and start_game.lower() != "no":
		print("Please enter the correct answer")
		start_game = input("Enter yes to start or no to stop playing:").lower()




while start_game.lower() != "no":

	user_input = int(input('enter "Guess my number between 1 and 1000 with the fewest guesses:". '))
	
	if user_input  > guess:
		print("too high. try again")
	elif user_input < guess:
		print("too low. try again")
	else:
		print("Congratulations. you guessed the number!")
		

	start_game = input("Enter yes to start or no to stop playing:")
	while start_game.lower() != "yes" and start_game.lower() != "no":
		print("Please enter the correct answer")
		start_game = input("Enter yes to start or no to stop playing:").lower()

print("Thank you for playing the game")
print("Application closes")

