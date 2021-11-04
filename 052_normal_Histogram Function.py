"""
Build a function that creates histograms. Every bar needs to be on a new line and its length corresponds to the numbers in the list passed as an argument. The second argument of the function represents the character that needs to be used.

histogram(lst, char) -> str
Examples
histogram([1, 3, 4], "#") ➞ "#\n###\n####"

#
###
####

histogram([6, 2, 15, 3], "=") ➞ "======\n==\n===============\n==="

======
==
===============
===

histogram([1, 10], "+") ➞ "+\n++++++++++"

+
++++++++++
Notes
For better understanding try printing out the result.
"""
def histogram(lst, char):

    # return '\n'.join(char * i for i in lst)

    return ''.join([char * x + '\n' for x in lst])[:-1]

    # result = ''
    # for i in range(len(lst)):
    #     result = result + lst[i] * char + '\n'
    # return result[:-1]

print(histogram([1, 3, 4], "#"))
print(histogram([2,4,5,6], "o"))
print(histogram([4,2], "*"))
print(histogram([20,1,12], "H"))
print(histogram([2,1,2,4,5,2,3], "#"))



