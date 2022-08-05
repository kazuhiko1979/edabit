"""
The Primiera
Primiera (from the french word prime, "prize") is a combination of cards of Scopa, a popular Italian card game.

For establishing the value of the Primiera, a separate point scale is used for selecting the best cards in the player's deck, in each of the four suits and totaling those four cards point values. A Primiera requires at least one card for each suit, otherwise, it can't be calculated.

This is the Primiera points scale:

7 is worth 21 points.
6 is worth 18 points.
Ace is worth 16 points.
Cards from 2 to 5 are worth 10 points plus the card value.
Face cards (Jack, Queen and King) are worth 10 points.
Create a function that takes in a list representing a cards deck and returns the value of the Primiera.

Examples
get_primiera_score(["Ad", "7d", "5h", "2c", "Ks"]) ➞ 58
# In the diamonds set 7 is higher than Ace (21 > 16).

get_primiera_score(["2d", "Jd", "7h", "Qc", "5s", "As"]) ➞ 59
# In the diamonds set 2 is higher than Jack (12 > 10), while in
# the spades set Ace is higher than 5 (16 > 15 ).

get_primiera_score(["2d", "Jd", "Qc", "5s", "As"]) ➞ 0
# There aren't cards in the hearts set, so Primiera can't be
# calculated.
Notes
Notation: Ace, card numbers from 2 to 7, Jack, Queen or King + diamonds, hearts, clubs or spades.
If one or more seeds are missing from the deck the value of the Primiera is equal to 0.
"""

def get_primiera_score(deck):

	if set(set(card[1] for card in deck)) != {'h', 'd', 's', 'c'}:
		return 0

	val = {'2':12,'3':13,'4':14,'5':15,'6':18,'7':21,'J':10,'Q':10,'K':10,'A':16}

	score = 0
	for i in 'hdcs':
		score += max([val[card[0]] for card in deck if card[1] == i])
	return score





print(get_primiera_score(["Ad", "7d", "5h", "2c", "Ks"]))