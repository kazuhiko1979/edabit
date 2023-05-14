"""
Mountains or Valleys
A mountain is a list with exactly one peak.

All numbers to the left of the peak are increasing.
All numbers to the right of the peak are decreasing.
The peak CANNOT be on the boundary.
A valley is a list with exactly one trough.

All numbers to the left of the trough are decreasing.
All numbers to the right of the trough are increasing.
The trough CANNOT be on the boundary.
Some examples of mountains and valleys:

Mountain A:  [1, 3, 5, 4, 3, 2]   # 5 is the peak
Mountain B:  [-1, 0, -1]   # 0 is the peak
Mountain B:  [-1, -1, 0, -1, -1]   # 0 is the peak (plateau on both sides is okay)

Valley A: [10, 9, 8, 7, 2, 3, 4, 5]   # 2 is the trough
Valley B: [350, 100, 200, 400, 700]  # 100 is the trough
Neither mountains nor valleys:

Landscape A: [1, 2, 3, 2, 4, 1]  # 2 peaks (3, 4), not 1
Landscape B: [5, 4, 3, 2, 1]  # Peak cannot be a boundary element
Landscape B: [0, -1, -1, 0, -1, -1]  # 2 peaks (0)
Based on the rules above, write a function that takes in a list and returns either "mountain", "valley", or "neither".

Examples
landscape_type([3, 4, 5, 4, 3]) ➞ "mountain"

landscape_type([9, 7, 3, 1, 2, 4]) ➞ "valley"

landscape_type([9, 8, 9]) ➞ "valley"

landscape_type([9, 8, 9, 8]) ➞ "neither"
Notes
A peak is not exactly the same as the max of a list. The max is a unique number, but a list may have multiple peaks. However, if there exists only one peak in a list, then it is true that the peak = max.
See comments for a hint.
"""
def landscape_type(lst):

	if any((sorted(lst[:i+1]) == lst[:i+1] and sorted(lst[i:], reverse=True) == lst[i:]) for i in range(1,len(lst)-1)):
		return 'mountain'
	elif any((sorted(lst[:i+1], reverse=True) == lst[:i+1] and sorted(lst[i:]) == lst[i:]) for i in range(1,len(lst)-1)):
	    return 'valley'
	return 'neither'


# def landscape_type(lst):
#
#     count = 0
#
#     # mountain
#     top_index = lst.index(max(lst))
#     if 0 < top_index < (len(lst) - 1) and not all([i if i < max(lst) else False for i in lst]):
#         # 最高地点1点確認
#         count_top = len([i for i, x in enumerate(lst) if x == max(lst)])
#         if count_top == 1:
#             count += 1
#         # 左右傾斜傾斜確認
#         if lst[:top_index] == sorted(lst[:top_index]):
#             pass
#         else:
#             count += 1
#         if lst[top_index + 1:] == sorted(lst[top_index + 1:], reverse=True):
#             pass
#         else:
#             count += 1
#         # return 'mountain' if count == 1 else "neither, {} peaks + boundary".format(count)
#         return 'mountain' if count == 1 else "neither"
#     # valley
#     bottom_index = lst.index(min(lst))
#     if bottom_index >= 1 and lst[0] > lst[bottom_index] < lst[-1]:
#         return 'valley'
#
#     # peaks + boundary
#     count_top = len([i for i, x in enumerate(lst) if x == max(lst)])
#     if sorted(lst) == sorted(lst, reverse=False) and count_top == 1:
#         # return "{}, {}".format("neither", 'boundary')
#         return "neither"
#
#     else:
#         # return "neither, {} peaks".format(count_top)
#         return "neither"


print(landscape_type([3, 4, 5, 4, 3]))
print(landscape_type([9, 7, 3, 1, 2, 4]))
print(landscape_type([9, 8, 9]))
print(landscape_type([9, 8, 9, 8]))
print(landscape_type([1, 3, 5, 4, 3, 2]))
print(landscape_type([-1, 0, -1]))
print(landscape_type([10, 9, 8, 7, 2, 3, 4, 5]))
print(landscape_type([350, 100, 200, 400, 700]))
print(landscape_type([-1, -1, 0, -1, -1]))
print(landscape_type([0, -1, -1, 0, -1, -1]))
print(landscape_type([1, 2, 3, 2, 4, 1]))
print(landscape_type([5, 4, 3, 2, 1]))
print(landscape_type([1, 2, 3, 4]))

