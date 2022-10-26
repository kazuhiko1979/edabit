"""
Briscola! (Part I)
Briscola is an Italian card game, played with a deck of 40 cards that has four suits (hearts, diamonds, clubs, and spades), so that there are ten cards per suit: the Ace, the numbered cards from 2 up to 7, and the three face-cards (Jack, Queen, and King). In this challenge, the notation used for the cards is a string containing the card value (with the upper-case initial for face-cards) and the lower-case initial for suits, as in the examples below:

Ah = Ace of Hearts
2s = Two of Spades
Jc = Jack of Clubs
Kd = King of Diamonds
The total number of points available is 120. When counting the points scored at the end of a game, the cards have the following values:

Ace: 11 points
Three: 10 points
King: 4 points
Queen: 3 points
Jack: 2 points
Any other card has no value (0 points).
Each game of Briscola is made of two rounds. After the first round, the points are counted for both you and your opponent, and these scores (plus 1) will set the target for winning the game, after that the second round is played.

- First Round -
Player score: 80
Opponent score: 40
- Second Round -
Player wins scoring 41 points or more.
Opponent wins scoring 81 points or more.
If after the second round the total points are equal for both you and your opponent, it's a tie.

- First Round -
Player score: 80
Opponent score: 40
- Second Round -
Player score: 40
Opponent score: 80

It's a tie! 120 points for both players.
You are given two lists as parameters:

my_deck1 contains your collected cards during the first round.
my_deck2 contains your collected cards during the second round.
You have to implement a function that returns:

"You Win!" if in the second round you totalized a higher score than your opponent's score in the first round.
"You Lose!" if in the second round you totalized a lower score than your opponent's score in the first round.
"Draw!" if after the second round the total points are the same for both you and your opponent.
Examples
briscola_score(
  ["3c", "3s", "Qd", "Jh", "5d", "Jc", "6d", "Ad", "Js", "Qc"],
  ["Jd", "Kd", "4c", "6s", "Ks", "5c", "3d", "As", "Jh", "6h"]
) ➞ "You Lose!"

# You score 43 points in the first round.
# You need to score at least 78 points in the second round.
# You score 33 points in the second round.

briscola_score(
  ["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
  ["3d", "Ad", "Ac", "As", "Ah"]
) ➞ "You Win!"

# You score 67 points in the first round.
# You need to score at least 54 points in the second round.
# You score 54 points in the second round.

briscola_score(
  ["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
  ["3d", "Ad", "Ac", "As", "3h"]
) ➞ "Draw!"

# You score 67 points in the first round.
# You need to score at least 54 points in the second round.
# You score 53 points in the second round.
# Your total score is 120, and so is for your opponent.
Notes
You don't need to count the points scored by your opponent, because you know the maximum points available in a round (120).
Despite suits are important during the game, they do not influence the score when counting points.
The original standard suits and face-cards of an Italian deck are different from the international ones used for Poker. If you want to know more, take a look at the Resources tab.
"""
# v2
def briscola_score(my_deck1, my_deck2):

	value = {'A': 11, '3': 10, 'K': 4, 'Q': 3, 'J': 2}
	score = sum([value.get(card[0], 0) for card in my_deck1 + my_deck2])
	if score > 120: return 'You Win!'
	if score < 120: return 'You Lose!'
	return 'Draw!'



# v1
# points = {'A': 11,
# 		  '3': 10,
# 		  'K': 4,
# 		  'Q': 3,
# 		  'J': 2
# 		  }
#
#
# def briscola_score(my_deck1, my_deck2):
#
# 	my_deck1 = sum(filter(None, [points.get(i[0]) for i in my_deck1]))
# 	my_deck2 = sum(filter(None, [points.get(i[0]) for i in my_deck2]))
#
# 	total = my_deck1 + my_deck2
# 	if total > 120:
# 		return "You Win!"
# 	if total == 120:
# 		return "Draw!"
# 	else:
# 		return "You Lose!"




print(briscola_score(
  ["3c", "3s", "Qd", "Jh", "5d", "Jc", "6d", "Ad", "Js", "Qc"],
  ["Jd", "Kd", "4c", "6s", "Ks", "5c", "3d", "As", "Jh", "6h"]
))

print(briscola_score(["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
					 ["3d", "Ad", "Ac", "As", "Ah"]))

print(briscola_score(["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
					 ["3d", "Ad", "Ac", "As", "3h"]))


print(briscola_score(["4h", "4s", "7s", "3d", "2c", "As", "3c", "4c","Ah", "7h", "Kc", "Jc", "Qh", "Jd", "Ks"], ["4s", "Ah", "Qh", "7c", "6s", "Js", "6d", "Qc","5d", "Kd", "3d", "Ac", "4c", "5s", "3h", "6h","As", "7d", "2s", "2c", "3c", "6c", "7h", "Kc"]))

print(briscola_score(["Js", "Qc", "2c", "Kc", "Kh", "7c", "5h", "Jh", "2s", "6d","4s", "4c", "Kd", "6s", "Ks", "Qh", "7s", "Jc", "5c", "5d","6c", "2h", "Ad", "7d", "Ah", "5s", "3s", "6h"], ["As", "3c", "Kd", "Ac", "Ah", "Ad", "Jh"]))
print(briscola_score(["3c", "3s", "Qd", "Jh", "5d", "Jc", "6d", "Ad", "Js", "Qc"], ["2s", "Kd", "3d", "6s", "Qc", "5c", "6d", "6h","6c", "5h", "Qd", "4s", "3c", "2h", "3s"]))