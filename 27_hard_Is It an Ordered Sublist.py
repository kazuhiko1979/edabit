"""
Is It an Ordered Sublist?
Given two lists smlst and biglst, we say smlst is an ordered sublist of biglst if all the elements of smlst can be found in biglst, and in the same order.

Examples:

[4, 3, 2] is an ordered sublist of [5, 4, 3, 2, 1].
[5, 3, 1] is an ordered sublist of [5, 4, 3, 2, 1].
[5, 3, 1] is not and ordered sublist of [1, 2, 3, 4, 5] since elements are not in the same - [1, 2, 3] is an ordered sublist of [3, 2, 1, 2, 3].
Write a function that, given lists smlst and biglst, decides if smlst is an ordered sublist of biglst.

Examples
is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]) ➞ True

is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]) ➞ True

is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]) ➞ False

is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]) ➞ True
Notes
Be careful of examples like the fourth example, where the elements of smlst appear multiple times in biglst.
"""

def is_ord_sub(smlst, biglst):

    # a = 0
    #
    # for i in smlst:
    #     if i in biglst[a:]:
    #         a += biglst[a:].index(i) + 1
    #     else:
    #         return False
    # return True

    i, j = 0, 0
    while i < len(smlst) and j < len(biglst):
        if smlst[i] == biglst[j]:
            i += 1
        j += 1

    print(i, j)
    print(i, len(smlst))
    return i == len(smlst)





    # boolSmlst = []
    # boolBiglst = []
    #
    # if smlst[0] != 0:
    #     boolSmlst.append("True")
    # else:
    #     boolSmlst.append("False")
    #
    # index = 0
    #
    #
    #
    # while index < len(smlst):
    #     try:
    #         if smlst[index] < smlst[index+1]:
    #             boolSmlst.append("True")
    #             index += 1
    #             continue
    #
    #         if smlst[index] > smlst[index+1]:
    #             boolSmlst.append("False")
    #             index += 1
    #             continue
    #         if smlst[index] == smlst[index+1]:
    #             boolSmlst.append("unchange")
    #             index += 1
    #             continue
    #     except:
    #         # print("indexError")
    #         index += 1
    #
    # # return boolSmlst
    #
    # if biglst[0] != 0:
    #     boolBiglst.append("True")
    # else:
    #     boolBiglst.append("False")
    #
    #
    #
    # big_index = 0
    #
    # while big_index < len(biglst):
    #     try:
    #         if biglst[big_index] < biglst[big_index+1]:
    #             boolBiglst.append("True")
    #             big_index += 1
    #             continue
    #
    #         if biglst[big_index] > biglst[big_index+1]:
    #             boolBiglst.append("False")
    #             big_index += 1
    #             continue
    #
    #         if biglst[big_index] == biglst[big_index+1]:
    #             boolBiglst.append("unchange")
    #             big_index += 1
    #             continue
    #     except:
    #         # print("indexError")
    #         big_index += 1
    #
    # # print(boolSmlst)
    # # print(boolBiglst)
    #
    # final = []
    # for x, y in zip(boolSmlst, boolBiglst):
    #     if x == y:
    #         final.append(x)
    #
    # strSmlst = ''.join([str(_) for _ in smlst])
    # strBiglst = ''.join([str(_) for _ in biglst])
    #
    # # print(strSmlst)
    # # print(strBiglst)
    #
    # return boolSmlst == final or strSmlst in strBiglst or biglst == [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1]


print(is_ord_sub([4, 3], [3, 4]))
print(is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]))
print(is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]))
print(is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]))
print(is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3])) # True
print(is_ord_sub([0, 1, 0, 1], [1, 0, 1, 0, 1])) # True
print(is_ord_sub([0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 1, 1, 0]))
print(is_ord_sub([0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]))
print(is_ord_sub([1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]))
print(is_ord_sub([1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1]))
