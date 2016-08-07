# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate_letter(letter, n):
	if letter.isupper():
		start = ord('A')
	elif letter.islower():
		start = ord('a')
	else:
		return letter

	# not done yet, need to figure out how to connect the two



def rotate_word(word, shift):
	shifted_string = " "
	for letter in word:
		shifted_string += rotate_letter(letter,n)
	return shifted_string