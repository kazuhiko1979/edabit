"""
Sort Characters by Frequency, Case, Alphabet
The function is given a string. Sort the characters and return a new string. Sorting conditions:

Most frequent (case-specific) move in front.
For the same frequency upper case characters move in front.
For the same frequency and case sort them alphabetically.
Examples
frequency_sort("tree") ➞ "eert"

frequency_sort("cccaaa") ➞ "aaaccc"

frequency_sort("Aabb") ➞ "bbAa"
"""

# v2

def frequency_sort(s):

    return ''.join(sorted(s, key=lambda x: (-s.count(x), -x.isupper(), x.lower())))

# v1
# import operator as op
#
# def frequency_sort(s):
#
#     temp = sorted([str(i) * int(op.countOf(s, i)) for i in list(set(sorted(s)))])
#     return ''.join(sorted(temp, key=lambda s: (-len(s))))



    # temp = sorted(temp, key=lambda s: (-len(s), s.isupper()))

    # def custom_key(str):
    #     return -len(str), str.lower()
    #
    # return ''.join(sorted(temp, key=custom_key))




print(frequency_sort("tree"))
print(frequency_sort("ccSctiXmStfmctmgfmfcfgtggEiicfiwtitgcgwScfXwScmwgtmfwigmifgfmSfwitgX"))
print("ffffffffffggggggggggccccccccciiiiiiiimmmmmmmmttttttttwwwwwwSSSSSXXXE")

print(frequency_sort("qqXQwlbYOboaooqXixQqQqiOBixaxQqQxbQaBqqyQhBQQwqOQqXX"))
print("QQQQQQQQQQqqqqqqqqqqXXXXxxxxBBBOOOaaabbbiiiooowwYhly")