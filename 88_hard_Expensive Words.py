"""
Expensive Words
Each letter in a sentence is worth its position in the alphabet (i.e. a = 1, b = 2, c = 3, etc...). However, if a word is all in UPPERCASE, the value of that word is doubled.

Create a function which returns the value of a sentence.

get_sentence_value("abc ABC Abc") ➞ 24
# a = 1, b = 2, c = 3

# abc = 1 + 2 + 3 = 6
# ABC = (1+2+3) * 2 = 12 (ALL letters are in uppercase)
# Abc = 1 + 2 + 3 = 6 (NOT ALL letters are in uppercase)

# 6 + 12 + 6 = 24
Examples
get_sentence_value("HELLO world") ➞ 176

get_sentence_value("Edabit is LEGENDARY") ➞ 251

get_sentence_value("Her seaside sea-shelling business is really booming!") ➞ 488
Notes
Ignore spaces and punctuation.
Remember that the value of a word isn't doubled unless all the letters in it are uppercase.
"""

import string

def get_sentence_value(txt):

  # alphabet = "abcdefghijklmnopqrstuvwxyz"

  # alpha_dict = {value: key for key, value in enumerate(alphabet, start=1)}
  #
  # txt = txt.split()
  # point = 0
  #
  # for word in txt:
  #   upper = word.isupper()
  #   word = word.lower()
  #   for w in word:
  #     if upper and w.isalpha():
  #       point += (alpha_dict[w] * 2)
  #     elif not upper and w.isalpha():
  #       point += alpha_dict[w]
  # return point



  up_txt = ''.join([i if i.isupper() else i.lower() for i in txt.split()])
  new_dict = {val: key for key, val in enumerate(string.ascii_lowercase, 1)}

  # res = []
  # for i in up_txt:
  #   if i.isalpha():
  #     if i.islower():
  #       res.append(new_dict.get(i))
  #     else:
  #       res.append(new_dict.get(i.lower())*2)
  #
  # return sum(res)

  # return sum([new_dict.get(i) if i.islower() else new_dict.get(i.lower())*2 for i in up_txt if i.isalpha()])


print(get_sentence_value("HELLO world"))
print(get_sentence_value("Edabit is LEGENDARY"))
print(get_sentence_value("Her seaside sea-shelling business is really booming!"))











