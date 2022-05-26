"""
Nearest Vowel
Given a letter, created a function which returns the nearest vowel to the letter. If two vowels are equidistant to the given letter, return the earlier vowel.

Examples
nearest_vowel("b") ➞ "a"

nearest_vowel("s") ➞ "u"

nearest_vowel("c") ➞ "a"

nearest_vowel("i") ➞ "i"
Notes
All letters will be given in lowercase.
There will be no alphabet wrapping involved, meaning the closest vowel to "z" should return "u", not "a".
"""

def nearest_vowel(s):

  # v1
  alphabets = "abcdefghijklmnopqrstuvwxyz"

  vowels = ["a", "e", "i", "o", "u"]
  vowels_index = [1, 5, 9, 15, 21]

  dict_alphabets = ({value: key for key, value in enumerate(alphabets, start=1)})

  for key, value in dict_alphabets.items():
    if key == s:
      for i in range(0, len(vowels_index)):
        vowels_index[i] = abs(value - vowels_index[i])
  return vowels[vowels_index.index(min(vowels_index))]


  # v2
  # alphabet = "abcdefghijklmnopqrstuvwxyz"
  # distances = [abs(alphabet.index(s) - alphabet.index(i)) for i in 'aeiou']
  #
  # return 'aeiou'[distances.index(min(distances))]

  # v3
  # return sorted([(abs(ord(s) - ord(x)), x) for x in 'aeiou'])[0][1]

  # V4
  # return min('aeiou', key=lambda v: abs(ord(s) - ord(v)))


print(nearest_vowel("b"))
print(nearest_vowel("s"))
print(nearest_vowel("c"))
print(nearest_vowel("i"))
print(nearest_vowel("r"))
print(nearest_vowel("y"))
print(nearest_vowel("z"))







