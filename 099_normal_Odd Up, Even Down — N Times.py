"""
Odd Up, Even Down — N Times
Create a function that performs an even-odd transform to a list, n times. Each even-odd transformation:

Adds two (+2) to each odd integer.
Subtracts two (-2) from each even integer.
Examples
even_odd_transform([3, 4, 9], 3) ➞ [9, -2, 15]
# Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]

even_odd_transform([0, 0, 0], 10) ➞ [-20, -20, -20]

even_odd_transform([1, 2, 3], 1) ➞ [3, 0, 5]
Notes
"""

def even_odd_transform(lst, n):

    # c = []
    #
    # for i in lst:
    #     if i % 2 == 0:
    #         c.append(i-2*n)
    #     else:
    #         c.append(i+2*n)
    # return c

    return [i + (n*2) if i % 2 else i - (n*2) for i in lst]


    # index_lst = 0
    # temp_n = n
    #
    # res = [0 for _ in range(0, len(lst))]
    #
    # while index_lst < len(lst):
    #     while temp_n > 0:
    #         if lst[index_lst] % 2 == 0:
    #             res[index_lst] = res[index_lst] - 2
    #             temp_n -= 1
    #         else:
    #             res[index_lst] = res[index_lst] + 2
    #             temp_n -= 1
    #
    #     index_lst += 1
    #     temp_n = n
    #
    # return list(map(lambda x, y: x + y, res, lst))


print(even_odd_transform([3, 4, 9], 3))
print(even_odd_transform([0, 0, 0], 10))
print(even_odd_transform([1, 2, 3], 1))
print(even_odd_transform([55, 90, 830], 2))





