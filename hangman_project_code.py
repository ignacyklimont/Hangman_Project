# Project: Hangman Game
# Python 3.10
# DATE: 22.07.2022
import random


# Class Hangman
class Hangman:

	def __init__(self, words, attempts):
		self.words = words
		self.attempts = attempts
		self.answer = random.choice(words)
		self.won_games = 0
		self.lost_games = 0
		self.guesses = set()
		self.hidden = ''

	def choose(self):
		choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: \n')
		if choice == 'play':
			game.start()
		elif choice == 'results':
			print(f'You won: {self.won_games} times.')
			print(f'You lost: {self.lost_games} times.')
			game.choose()
		elif choice == 'exit':
			quit()
		else:
			game.choose()

	def start(self):
		while self.attempts > 0:
			self.hidden = ''.join(let if let in self.guesses else '-' for let in self.answer)
			print(self.hidden)
			if '-' not in self.hidden:
				print(f'You guessed the word {self.answer}!')
				print('You survived!')
				self.won_games += 1
				self.answer = random.choice(self.words)
				self.hidden = ''
				self.guesses.clear()
				game.choose()
			guess = input('Input a letter: ')
			if len(guess) != 1:
				print('Please, input a single letter.')
			elif not guess.islower():
				print('Please, enter a lowercase letter from the English alphabet.')
			elif guess in self.guesses:
				print(f"You've already guessed this letter.")
			elif guess not in self.answer:
				self.attempts -= 1
				print(f"That letter doesn't appear in the word. # {self.attempts} attempts")
			self.guesses.add(guess)
		print("You lost!")
		self.lost_games += 1
		self.answer = random.choice(self.words)
		self.hidden = ''
		self.guesses.clear()
		game.choose()


# Initializing the game
if __name__ == '__main__':
	config = {'words': ['python', 'java', 'swift', 'javascript'], 'attempts': 8}
	game = Hangman(**config)
	game.choose()
