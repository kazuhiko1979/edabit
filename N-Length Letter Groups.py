"""
Write a function that returns a list of strings populated from the slices of n-length characters of the given word (a slice after another while n-length applies onto the word).

Examples
collect("intercontinentalisationalism", 6)
➞ ["ationa", "interc", "ntalis", "ontine"]

collect("strengths", 3)
➞ ["eng", "str", "ths"]

collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)
➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]
Notes
Ensure that the resulting array is lexicographically ordered.
Return an empty array if the given string is less than n.
A recursive version of this challenge can be found via this link.
"""


def collect(s, n):

    return sorted([s[n*i:n*(i+1)] for i in range(0, int(len(s) / n))])

    # print(len(s))
    # print(s)
    # cuts = math.floor(len(s) / n)
    # print(cuts)
    # s_cuts = s[:-cuts]
    # print(s_cuts)
    # print([s_cuts[n*i:n*(i+1)] for i in range(0, cuts)])


print(collect("intercontinentalisationalism", 6))
print(collect("strengths", 3))
print(collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15))













