
print """Welcome To The Hangman Game!
Guess the secret word one letter at a time.."""

word =  "hangman"
word = word.lower()

#define exceptions

class Error(Exception):
	"""The base class for the game derived from the parent Exception class"""
	pass

class NoInputErr(Error):
	"""Raised when the user fails to enter any character in the prompt"""
	pass
class MoreThanOneCharacterErr(Error):
	"""Raised when the user enters more than one character"""
	pass

class NotAlphaErr(Error):
	"""Raised when the input character from the user is not an alphabet character"""
	pass
	
class AlreadyGuessedErr(Error):
	"""Raised when the input character from the user has been guessed already"""
	pass	

	
#main game

def hangman_game(word):
	wrd = [c for c in word]
	misses = ["________ " , "|  |" , "|  0" , "| /|\ " , "| / \ " , "| " ]
	count = 0
	loose_msg = "You loose!"
	win_msg = "\nYOU WIN!"
	mask = "_" * len(word)
	word_rep = [c for c in mask]
	
	while True:
		if count == len(misses):
			print loose_msg
			break
		elif "".join(word_rep) == word:
			print win_msg
			break
			
		try:	
			input = raw_input("\nEnter letter > ")
			if not input:
				raise NoInputErr
			elif not input.isalpha():
				raise NotAlphaErr
			elif len(input) > 1:
				raise MoreThanOneCharacterErr
			elif input in word_rep:
				raise AlreadyGuessedErr
        
		except NoInputErr:
			print "You didn't enter any character"
			continue
		except MoreThanOneCharacterErr:
			print("Please enter only one character")
			continue
		except NotAlphaErr:
			print("Please enter only a character in the alphabet")
			continue
		except AlreadyGuessedErr:
			print("You already guessed that character. Try guessing another one")
			continue
		
		#work with lower case as in word
		input = input.lower()  	
		
		if input not in wrd:
			count += 1
			for c in misses[:count]:
				print c
			continue		
		elif input in word:
			while input in wrd:
				indx = wrd.index(input) 
				word_rep[indx] = input
				wrd[indx] = "$"
			for_print = [c + " " for c in word_rep]
			print "\nYou guessed correctly a character in the word:",
			print "".join(for_print)
			continue
						
			
hangman_game(word)				

print ""

#Ask the user if they wants to play again

def play_again(value = raw_input("Would you like to play again?: Y/N > ")): 
	value = value.upper()
	if value == "Y":
		print("\nGood Luck On Another Try!!\n")
		hangman_game(word)
	else:
		pass
		

play_again()		
