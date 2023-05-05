"""
Text Twist!
In Text Twist, players try to score points by forming words using the letters from a 6-letter scrambled word. They win the round if they can successfully unscramble the 6-letter word.

Create a function that takes in an array of already-guessed words, the unscrambled 6-letter word and returns the total number of points the player scored in a particular round using the following rubric:

3-letter words are 1 pt
4-letter words are 2 pts
5-letter words are 3 pts
6-letter words are 4 pts + 50 pt bonus (for unscrambling the word)
Remember that invalid words (words that cannot be formed from the 6-letter unscrambled words) count as 0 pts.

Examples
total_points(["cat", "create", "sat"], "caster") ➞ 2
# Since "create" is an invalid word.

total_points(["trance", "recant"], "recant") ➞ 108
# Since "trance" and "recant" score 54 pts each.

total_points(["dote", "dotes", "toes", "set", "dot", "dots", "sted"], "tossed") ➞ 13
# Since 2 + 3 + 2 + 1 + 1 + 2 + 2 = 13
Notes
If a 6-letter word has multiple anagrams, count each 6-letter unscramble as an additional 54 pts. For example, if the word is arches, and the player guessed arches and chaser, add 108 pts for both words.
You can play Text Twist here: http://text-twist2.com
"""

# v1
def total_points(guesses, word):

	point = 0

	for guess in guesses:

		dic_guess = {}
		for char in list(guess):
			dic_guess[char] = dic_guess.get(char, 0) + 1

		dic_word = {}
		for char in list(word):
			dic_word[char] = dic_word.get(char, 0) + 1

		if len(dic_guess) == 6 and len(dic_word) == 6 and sorted(dic_guess) == sorted(dic_word):
			point += 54
		else:
			valid_guess = True

		# result = []
		for char, freq in dic_guess.items():
			if char not in dic_word or dic_word[char] < freq:
				valid_guess = False
				break
			# GitHubから編集

		# if all(result):
		if valid_guess:
			point += len(guess) - 2
	return point




print(total_points(["dote", "dotes", "toes", "set", "dot", "dots", "sted"], "tossed"))
print(total_points(["dial", "tail", "lid", "tide", "date", "late", "tad"], "detail"))
print(total_points(["trance", "recant"], "recant"))
print(total_points(["bluest", "sublet", "let", "set", "belt", "belts", "bet", "bets", "sted", "but", "tule"], "subtle"))
print(total_points(["cat", "create", "sat"], "caster"))
print(total_points(["emote", "tome", "root"], "meteor"))
