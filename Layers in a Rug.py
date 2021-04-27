"""
Write a function that counts how many concentric layers a rug.

Examples
count_layers([
  "AAAA",
  "ABBA",
  "AAAA"
]) ➞ 2

count_layers([
  "AAAAAAAAA",
  "ABBBBBBBA",
  "ABBAAABBA",
  "ABBBBBBBA",
  "AAAAAAAAA"
]) ➞ 3

count_layers([
  "AAAAAAAAAAA",
  "AABBBBBBBAA",
  "AABCCCCCBAA",
  "AABCAAACBAA",
  "AABCADACBAA",
  "AABCAAACBAA",
  "AABCCCCCBAA",
  "AABBBBBBBAA",
  "AAAAAAAAAAA"
]) ➞ 5
Notes
Multiple layers can share the same component so count them separately (example #2).
Layers will be horizontally and vertically symmetric.
There will be at least one layer for each rug.
"""

rug = [
"FFFFFFFFFFFFFFFFFFFFFFFFF",
"FFFFFFFFFFFFFFFFFFFFFFFFF",
"FFFFGGGGGGGGGGGGGGGGGFFFF",
"FFFFGGGAAAAAAAAAAAGGGFFFF",
"FFFFGGGAABBBBBBBAAGGGFFFF",
"FFFFGGGAABCCCCCBAAGGGFFFF",
"FFFFGGGAABCDDDCBAAGGGFFFF",
"FFFFGGGAABCDDDCBAAGGGFFFF",
"FFFFGGGAABCDDDCBAAGGGFFFF",
"FFFFGGGAABCCCCCBAAGGGFFFF",
"FFFFGGGAABBBBBBBAAGGGFFFF",
"FFFFGGGAAAAAAAAAAAGGGFFFF",
"FFFFGGGGGGGGGGGGGGGGGFFFF",
"FFFFFFFFFFFFFFFFFFFFFFFFF",
"FFFFFFFFFFFFFFFFFFFFFFFFF"
]

count = 1

for i in range(len(rug)//2):
    if rug[i] != rug[i+1]:
        count += 1
print(count)


