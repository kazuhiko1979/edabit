"""
Needle in a Hex String
Find the index of a string within a hex encoded string.

You will be given a string which needs to be found in another string which has previously been translated into hex. You will need to return the first index of the needle within the hex encoded string.

Examples
first_index("68 65 6c 6c 6f 20 77 6f 72 6c 64", "world") ➞ 6

first_index("47 6f 6f 64 62 79 65 20 77 6f 72 6c 64", "world") ➞ 8

first_index("42 6f 72 65 64 20 77 6f 72 6c 64", "Bored") ➞ 0
"""


def first_index(hex_txt, needle):


    # top_index_of_need = str(hex(ord(needle[0])))[2:]
    # return hex_txt.split().index(top_index_of_need)


    # return ''.join(chr(int(i, 16)) for i in hex_txt.split()).index(needle)



    # top_index_of_need = str(hex(ord(needle[0])))[2:]
    #
    # list = hex_txt.split(' ')
    #
    # for i in list:
    #     if i == top_index_of_need:
    #         return list.index(i)


print(first_index("68 65 6c 6c 6f 20 77 6f 72 6c 64", "world"))
print(first_index("a3 24 25 2d 2d 2d a3 24 20 77 6f 72 6c 64 2d 2d 2d", "world"))
print(first_index("42 6f 72 65 64 20 77 6f 72 6c 64", "Bored"))