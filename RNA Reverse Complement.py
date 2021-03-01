"""
Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:

original -> complement
"AAA" -> "UUU"
"UUU" -> "AAA"
"GGG" -> "CCC"
"CCC" -> "GGG"
"GGAACC" -> "CCUUGG"
Your function should find the complement on the right AND also reverse the resulting string.

Examples
reverse_complement("GUGU") ➞ "ACAC"
reverse_complement("UCUCG") ➞ "CGAGA"
reverse_complement("CAGGU") ➞ "ACCUG"
Notes
Assume all input seqeuences are valid.
"""
import string


def reverse_complement(input_sequence):

    first = "AUGC"
    second = "UACG"

    table = input_sequence.maketrans(first, second)
    table.update(input_sequence.maketrans(second, first))
    return ''.join(list(reversed(input_sequence.translate(table))))


print(reverse_complement("GUGU"))
print(reverse_complement("UCUCG"))
print(reverse_complement("CAGGU"))