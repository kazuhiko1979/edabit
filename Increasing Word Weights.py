"""
The weight of an English word can be calculated by summing the ASCII code point for each character in the word, excluding any punctuation:

"Wouldn't" = 87 + 111 + 117 + 108 + 100 + 110 + 116 = 749
Write a function that takes a sentence as a string, returning True if all word weights increase for each word in the sentence, and False if any word weight decreases or remains the same. For any single-word sentences, return True.

Examples
increasing_word_weights("Why not try?") ➞ True
# 312 -> 337 -> 351 (weights increase)

increasing_word_weights("All other roads.") ➞ False
# 281 -> 546 -> 537 (537 is less than 546)
"""
import re


def increasing_word_weights(sentence):

    sentence = re.sub(r"[^a-zA-Z']", " ", sentence).split(' ')
    sentence = [a for a in sentence if a != '']

    sub_total = []
    total = []

    for i in sentence:
        for j in i:
            sub_total.append(ord(j))
        sub_total = sum(sub_total)
        total.append(sub_total)
        # sub_total clear
        sub_total = []

    return total == sorted(total)


print(increasing_word_weights("Why not try?"))
print(increasing_word_weights("All other roads."))
print(increasing_word_weights("Face your fears, never settle."))
print(increasing_word_weights("Inconceivable!"))
print(increasing_word_weights("DON'T SHOUT!"))


