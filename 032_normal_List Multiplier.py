"""
Create a function that takes a list as an argument and returns a new nested list for each element in the original list. The nested list must be filled with the corresponding element (string or number) in the original list and each nested list has the same amount of elements as the original list.

Examples
multiply([4, 5]) ➞ [[4, 4], [5, 5]]

multiply(["*", "%", "$"]) ➞ [["*", "*", "*"], ["%", "%", "%"], ["$", "$", "$"]]

multiply(["A", "B", "C", "D", "E"]) ➞ [["A", "A", "A", "A", "A"], ["B", "B", "B", "B", "B"], ["C", "C", "C", "C", "C"], ["D", "D", "D", "D", "D"], ["E", "E", "E", "E", "E"]]
Notes
The given list contains numbers or strings.
"""

def multiply(l):

    return [[i]*len(l) for i in l]

    # degitsList = []
    #
    # string = "".join([''.join(str(i) for i in l)])
    #
    # if not string.isdigit():
    #     noDigitList = [[str(i) * len(l)] for i in l]
    #     return [list(''.join(noDigit)) for noDigit in noDigitList]
    # else:
    #     for s in l:
    #         l = str(s) * len(string)
    #         degitsList.append([int(i) for i in l])
    # return degitsList




    # l = [[str(i) * len(l)] for i in l]
    # print(l)

    # l = [list(''.join(i)) for i in l]
    # print(l)
    # for s in l:
    #     for i in s:
    #         print(int(i))
    #

    # [s for s in i for i in l]


     # return [list(''.join(i)) for i in l]


print(multiply([4, 5]))
print(multiply(["*", "%", "$"]))
print(multiply(["A", "B", "C", "D", "E"]))
print(multiply([1]))