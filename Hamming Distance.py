"""
Hamming distance is the number of characters that differ between two strings.

To illustrate:

String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.

Examples
hamming_distance("abcde", "bcdef") ➞ 5
hamming_distance("abcde", "abcde") ➞ 0
hamming_distance("strong", "strung") ➞ 1
"""
def hamming_distance(txt1, txt2):

    diff = 0
    for i, x in zip(txt1, txt2):
        if i != x:
            diff += 1
    return diff


print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))



