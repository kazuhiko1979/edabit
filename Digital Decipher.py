"""
In Digital Decipher, decoding is done by the simple subtraction of numbers in the key and the corresponding characters on a given list. You may want to solve this challenge before proceeding further.

Create a function that takes two arguments; a positive integer and a list of integers and returns a decoded message as string.

Assign a unique number to each letter of the alphabet.

 a  b  c  d  e  f  g  h  i  j  k  l  m
 1  2  3  4  5  6  7  8  9  10 11 12 13
 n  o  p  q  r  s  t  u  v  w  x  y  z
 14 15 16 17 18 19 20 21 22 23 24 25 26
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:

eMessage = [20, 12, 18, 30, 21]
key = 1939

digital_decipher(eMessage, key) ➞ "scout"
Subtract each key digit from eMessage consecutive digits:

  20 12 18 30 21
-  1  9  3  9  1
 ---------------
  19  3 15 21 20
Write the corresponding number against each character:

 s  c  o  u  t
19  3 15 21 20
See the below example for a better understanding:

eMessage = [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
key = 1939

digital_decipher(eMessage, key) ➞ "masterpiece"

  14 10 22 29  6 27 19 18  6  12 8
-  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  13  1 19 20  5 18 16  9  5  3  5
   m  a  s  t  e  r  p  i  e  c  e
Examples
digital_decipher([20, 12, 18, 30, 21], 1939) ➞ "scout"
digital_decipher([14, 30, 11, 1, 20, 17, 18, 18], 1990) ➞ "mubashir"
digital_decipher([6, 4, 1, 3, 9, 20], 100) ➞ "edabit"
"""
def digital_decipher(eMessage, key):
    alphabet = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l",
              13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w",
              24: "x", 25: "y", 26: "z"}

    key = str(key)
    current_index = 0
    x = ""

    for index, i in enumerate(eMessage):
        i = i - int(key[current_index])
        current_index += 1
        if current_index == len(key):
            current_index = 0
        x += alphabet[i]
    return x

print(digital_decipher([20, 12, 18, 30, 21], 1939))
print(digital_decipher([14, 30, 11, 1, 20, 17, 18, 18], 1990))
print(digital_decipher([6, 4, 1, 3, 9, 20], 100))




