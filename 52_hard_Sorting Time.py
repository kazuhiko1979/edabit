"""
Sorting Time
Python has a beautiful built-in function sorted that sorts an iterable, usually an array of numbers, sorting them in ascending order, but using key= you can sort the iterable in different ways.

Create a function that takes an array of integers as an argument and returns the same array in ascending order. Using sorted() would be easy, but for this challenge YOU have to sort the array creating your own algorithm.

Examples
sort_array([2, -5, 1, 4, 7, 8]) ➞ [-5, 1, 2, 4, 7, 8]

sort_array([23, 15, 34, 17, -28]) ➞ [-28, 15, 17, 23, 34]

sort_array([38, 57, 45, 18, 47, 39]) ➞ [18, 38, 39, 45, 47, 57]
Notes
The arrays can contain either positive or negative elements.
The arrays will only contain integers.
The arrays won't contain duplicate numbers.
"""

def sort_array(lst):

    return [lst.pop(lst.index(min(lst))) for i in range(len(lst))]



    # slst = []
    # while True:
    #     slst.append(min(lst))
    #     lst.remove(min(lst))
    #     if lst == []:
    #         return slst



    # Bublle sort
    # for i in range(len(lst)-1, 0, -1):
    #     for i_index in range(i):
    #         if lst[i_index] > lst[i_index+1]:
    #             temp = lst[i_index]
    #             lst[i_index] = lst[i_index + 1]
    #             lst[i_index+1] = temp
    #
    # return lst


    # selection sort
    # for i in range(len(lst)):
    #     min_index = i
    #     for j in range(i+1, len(lst)):
    #         if lst[min_index] > lst[j]:
    #             min_index = j
    #
    #     # Swap the minimum value with the compared value
    #     lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst

print(sort_array([2, -5, 1, 4, 7, 8]))
print(sort_array([23, 15, 34, 17, -28]))