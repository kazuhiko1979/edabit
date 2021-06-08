"""
Write a function that sorts a list of integers by their digit length in descending order, then settles ties by sorting numbers with the same digit length in ascending order.

Examples
digit_sort([77, 23, 5, 7, 101])
➞ [101, 23, 77, 5, 7]

digit_sort([1, 5, 9, 2, 789, 563, 444])
➞ [444, 563, 789, 1, 2, 5, 9]

digit_sort([53219, 3772, 564, 32, 1])
➞ [53219, 3772, 564, 32, 1]
"""
import operator

# keys = dict.fromkeys(['number', 'length'])
# numbers = [77, 23, 5, 7, 101]
# lengths = ([len(str(num)) for n, num in enumerate(numbers)])

lst = [77, 23, 5, 7, 101]

# dic = []
# for i, j in zip(numbers, lengths):
#     keys['number'] = i
#     keys['length'] = j
#     dic.append(keys.copy())
# print(dic)
#
# tmp = []
# lst = []
# for i, j in zip(numbers, lengths):
#     tmp.append(i)
#     tmp.append(j)
#         print(tmp)
# for x in tmp:
#     lst.append(tmp)
# print(lst)





# sorted_data = sorted(dic, key=lambda x:(x[0], x[1]))
# print(sorted(dic, key=operator.itemgetter('number'), reverse=True))

# for j in lengths:
#     keys['length'] = j
#     print(keys)

# dic = {"number": 77, 'length': 2}


# for n, num in enumerate(keys):
#     print(len(str(num)), num)

# dic = {key: length for key, length in zip(keys, lengths)}
# print(dic)
#
# # sorted(dic, key=lambda x:(x[0],x[1]), reverse=True)
#
# # print(sorted(dic.items(), key=lambda x:(x[0],x[1]), reverse=True))
# print([t[0] for t in sorted(dic.items(), key=lambda x:(x[0]))])
#
# print([key for key, val in sorted(dic.items(), key=lambda x:(x[1],x[1]), reverse=True)])
# print([key for key, val in sorted(dic.items(), reverse=True)])


print(sorted(sorted(lst), key=lambda x:len(str(x)), reverse=True))

