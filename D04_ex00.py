#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import sys
import random

# Body
#set variables
max_number = 25
answer = random.randint(1, max_number)
prompt = "Guess a number: "
guesses_left = 5

#begin program
while guesses_left > 0:
	guess_string = input(prompt)

	#check to see if input is an integer
	try:
		guess_int = int(guess_string)
	except:
		print('Nice try, enter a number: ')
	else:
		valid_input = (0 < guess_int <= max_number)

	if not valid_input:
		print("Invalid input. Looking for a number between 1 and 25.")
	else:
		guesses_left -= 1
		#if you ran out of guesses, tell them so and end program
		if guesses_left == 0:
			print("Sorry you ran out of guesses")
			break
		#if guess matched, tell them so, end program, otherwise have them try again until
		if guess_int == answer:
			print("Congratulations!")
			break
		else:
			print("Try again")
		
		if guess_int < answer:
			prompt = "Guess a higher number: "
		else:
			prompt = "Guess a lower number: "
		







################################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()