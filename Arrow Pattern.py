"""
Create a function that creates a pattern as a 2D list for a given number.

Examples
 >
 >>
 >>>
 >>
 >
"""
"""
arrow(3) ➞ [">", ">>", ">>>", ">>", ">"]
 >
 >>
 >>>
 >>>>
 >>>>
 >>>
 >>
 >

arrow(4) ➞ [">", ">>", ">>>", ">>>>", ">>>>", ">>>", ">>", ">"]
"""
# def arrow(num):
#
#     list = []
#     # Total no of rows
#     if num % 2 == 0:
#         for i in range(num + num):
#             size = i
#             if i >= num:
#                 size = num + num - i - 1
#
#             # cols in each row
#             for j in range(size + size + 1):
#                 if j < size:  # For printing space
#                     print('', end='')
#                 else:  # For printing *
#                     print('>', end='')
#
#             print()
#     else:
#         # Total no of rows
#         for i in range(num + num - 1):
#             size = i
#             if i >= num:
#                 size = num + num - i - 2
#
#             # cols in each row
#             for j in range(size + size + 1):
#                 if j < size:  # For printing space
#                     print('', end='')
#                 else:  # For printing *
#                     print('>', end='')
#             print()
#
#
# arrow(3)
# arrow(4)

def arrow(num):

    a = ['>' * i for i in range(1, num + 1)]
    # print(a)
    if num % 2 == 0:
        return a + a[::-1]
    return a + a[:-1][::-1]

    # count_list = [i for i in range(1, num+1)]
    # list = []
    #
    # if num % 2 == 0:
    #     for i in count_list:
    #         list.append(">" * i)
    #         if i == num:
    #             for j in reversed(count_list):
    #                 list.append(">" * j)
    # else:
    #     for i in count_list:
    #         list.append(">" * i)
    #     count_list.pop()
    #     for j in reversed(count_list):
    #         list.append(">" * j)
    # return list

print(arrow(3))
print(arrow(4))
print(arrow(5))
print(arrow(6))

