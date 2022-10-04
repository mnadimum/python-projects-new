# Guess the number (computer game)

import random

def guess(x):
	random_number = random.randint(1, x)
	guess = 0
	while guess != random_number:
		guess = int(input("Guess a number between 1 and 10 : "))
		if guess < random_number:
			print("Sorry, Guess is too low: ")
		elif guess > random_number:
			print("Sorry, Guess is too high: ")
	print(f"Yeah, Congrats, You have guessed the number {random_number} Correctly !!")
	
guess(10)
