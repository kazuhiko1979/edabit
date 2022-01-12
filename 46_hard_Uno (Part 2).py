"""
Uno (Part 2)
This problem is a continuation of Uno Part 1 (although you don't need to complete that problem to complete this one).

It's your turn to play again. Create a function that takes as its arguments (1) your hand (a list of cards), and (2) the face-up card. In Uno, you are able to play a card from your hand if either:

One of the card colors in your hand matches the face-up card's color.
One of the card numbers in your hand matches the face-up card's number.
Write a function that will return:

"Uno!" if after playing your card, you are left with a single card.
"You won!" if after playing your card, you are left with zero cards (an empty list).
"Keep going..." otherwise.
Examples
decision(["yellow 3", "red 3"], "red 10") ➞ "Uno!"

decision(["blue 1"], "blue 5") ➞ "You won!"

decision(["blue 1", "green 2", "yellow 4", "red 2"], "blue 5") ➞ "Keep going..."
"""

def decision(hand, face):

    f = face.split()
    if any(c.startswith(f[0]) or c.endswith(f[1]) for c in hand):
        hand.pop()
    return "Uno!" if len(hand) == 1 else "You won!" if len(hand) == 0 else "Keep going..."



    # if len(hand) > 2:
    #     return "Keep going..."
    #
    # if face.split()[0] in ' '.join(hand) or face.split()[1] in ' '.join(hand):
    #     hand.pop()
    #
    # return ["You won!", "Uno!"][len(hand)]



    # for card in hand:
    #     if card.split()[0] == face.split()[0]:
    #         hand.remove(card)
    #     if card.split()[1] == face.split()[1]:
    #         hand.remove(card)
    # return "Uno!" if len(hand) == 1 else "You won!" if len(hand) == 0 else "Keep going..."


print(decision(["yellow 3", "red 3"], "red 10"))
print(decision(["blue 1"], "blue 5"))
print(decision(["blue 1", "green 2", "yellow 4", "red 2"], "blue 5"))
print(decision(['red 1', 'blue 10'], 'blue 5'))

