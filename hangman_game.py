class Hangman:
	"""
	attributes:
  
	word: The secret word of the game
	mask: A clone of the word that replaces each letter with an underscore to mask what has not been guessed yet. 
		  letters guessed will be shown.
	guess: The character that the user guesses.	
	steps: A list with characters that represent the steps leading to 'game over'.
	misses: keeps track of the number of times the user guesses a wrong character. 
	name: The name of the user
  
  	

	"""

	def __init__(self, word):
		self.word = [c for c in word.lower()]
		self.mask = [c.replace(c, "_") for c in self.word]
		self.steps = ["________ " , "|  |" , "|  0" , "| /|\ " , "| / \ " , "| " ]
		self.misses = 0
		self.name = raw_input("Enter your name: ")
	
	def right_guess(self):
		
		"""
		 checks if the user's guess is correct and prints out an updated mask. 
		   > initializes variable indx to the index of guess
		   > replaces underscore in mask with the guessed character.
		   > adds a dollar sign to guessed character in word. This, in a loop case, will allow 
				for picking the index of the next same guessed character in word using the index method 
		"""
		
		while self.guess in self.word:
				
				indx = self.word.index(self.guess) 
				self.mask[indx] = self.guess
				self.word[indx] = "$"
			
		print("You guessed correctly. Here's your progress: "),
		print " ".join(self.mask)
		
	def wrong_guess(self):
		
		""" checks if the user's guess is incorrect, increments guesses and prints out the steps."""
		
		if self.guess not in self.word:
			
			self.misses += 1
			
			print(" letter [%s] is not in the word.\n") % self.guess
			
			for s in self.steps[ : self.misses ]:
				print(s)
		else:
			self.right_guess()   
	
			
	def prompt(self):
		
		""" prompts the user to guess a letter in the word and checks for exceptions."""
		
		while True:

			self.guess = raw_input("\n Guess a character in the word: > ").lower()
			print ""	
			
			if not self.guess:
				print("\n You didn't enter any character")
				
			elif not self.guess.isalpha():
				print("\n Please enter only a character in the alphabet")
		
			elif len(self.guess) > 1:
				print("\n Please enter only one character")
			
			elif self.guess in self.mask:
				print("\n You guessed that already! Try another guess")
			
			else:
				break	 
			
		return self.guess
		self.wrong_guess()
	
	def win(self):
		
		""" checks if the user has won and prints a message """
		
		if "_" not in self.mask:
			print("You win!")
			return True
					
	def lose(self):
		
		"""checks if the user has lost and prints a message"""
		
		if self.misses == len(self.steps):
			print("You lost!"),
			return True
			
	def play_game(self):
		
		"""bringing it all together :) """
		
		print "\n Welcome To The Hangman Game %s! \n" %self.name	
		while True:
			
			if self.win():
				break
				
			elif self.lose():
				break
				
			self.prompt()
			self.wrong_guess()
			
		
if __name__ == "__main__":
	
	game_round = Hangman("python")
	game_round.play_game()
