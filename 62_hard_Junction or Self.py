"""
Junction or Self?
In this challenge, you have to separate integers into two families, establishing if they are Junction Numbers or Self Numbers. Given a number n:

If exists at least a single number which added to the sum of its digits is equal to n, then n is a Junction Number.

If there are not numbers which added to the sum of their digits are equal to n, then n is a Self Number.

Given a positive integer n, implement a function that returns:

The string "Self" if n is a Self Number.
If n is a Junction Number an array, ordered descendingly, containing the numbers which generate n.
Examples
junction_or_self(25) ➞ [17]
# If we add 17 to the sum of its digits...
# ...17 + 1 + 7 = 25
# 25 is a Junction Number

junction_or_self(818) ➞ [805, 796]
# If we add 805 to the sum of its digits...
# ...805 + 8 + 0 + 5 = 818
# If we add 796 to the sum of its digits...
# ...796 + 7 + 9 + 6 = 818
# 818 is a Junction Number

junction_or_self(7) ➞ "Self"
# 1 + 1 = 2
# 2 + 2 = 4
# 3 + 3 = 6
# No number added to its own digits is equal to 7
# 7 is a Self Number
Notes
As in example #3, the sum of the digits of a positive integer lower than 10 is equal to that same integer.
By the formal definition, a Junction number must have at least two other numbers that generate it, so that the Instructions are to be considered valid only for this specific challenge.
You can expect only valid data as input.
Trivia: the first Junction Number that can be generated by three different numbers is 10000000000001, while the first generated by four different numbers is 1000000000000000000000102.
"""
def junction_or_self(n):

    junction = [k for k in range(n, -1, -1) if k + sum(map(int, str(k))) == n]
    return junction or "Self"


    # result = []
    #
    # for i in range(1, n):
    #     if i + sum(int(j) for j in str(i)) == n:
    #         result.append(i)
    # return sorted(result, reverse=True) if result else "Self"


    # result = []
    # sub_total = 0
    #
    # for i in range(1, n+1):
    #     for x in str(i):
    #         sub_total += int(x)
    #         junction = i + int(sub_total)
    #     sub_total = 0
    #
    #     if junction == n:
    #         result.append(i)
    #
    # if result:
    #     return sorted(result, reverse=True)
    # else:
    #     return "Self"

print(junction_or_self(7))
print(junction_or_self(25))
print(junction_or_self(11))
print(junction_or_self(818))
print(junction_or_self(117))
print(junction_or_self(309))
print(junction_or_self(20))




