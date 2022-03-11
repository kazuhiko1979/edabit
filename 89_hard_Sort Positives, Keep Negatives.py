"""
Sort Positives, Keep Negatives
Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.

Examples
pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]

pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]

pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]

pos_neg_sort([]) ➞ []
Notes
If given an empty list, you should return an empty list.
Integers will always be either positive or negative (0 isn't included in the tests).
"""

def pos_neg_sort(lst):

  # v1
  positive = sorted([i for i in lst if i > 0], reverse=True)

  # リスト（Positive)から最後尾から貼り付け
  result = []

  # for j in lst:
  #   if j > 0:
  #     result.append(positive.pop())
  #   else:
  #     result.append(j)
  # return result
  #
  # return [positive.pop() if j > 0 else j for j in lst]

  # v2
  positive = iter(sorted(i for i in lst if i > 0))
  return [next(positive) if i > 0 else i for i in lst]


  # v0
  # return [positive.pop() if j > 0 else j for j in lst]

  # positive = sorted([i for i in lst if i > 0])
  #
  # for index, value in enumerate(lst):
  #     if value < 0:
  #       positive.insert(index, value)
  # return positive


print(pos_neg_sort([6, 3, -2, 5, -8, 2, -2]))
print(pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]))
print(pos_neg_sort([-5, -5, -5, -5, 7, -5]))
print(pos_neg_sort([]))


