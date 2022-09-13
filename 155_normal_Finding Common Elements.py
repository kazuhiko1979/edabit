"""
Finding Common Elements
Create a function that takes two lists of numbers sorted in ascending order and returns a list of numbers which are common to both the input lists.

Examples
common_elements([-1, 3, 4, 6, 7, 9], [1, 3]) ➞ [3]

common_elements([1, 3, 4, 6, 7, 9], [1, 2, 3, 4, 7, 10]) ➞ [1, 3, 4, 7]

common_elements([1, 2, 2, 2, 3, 4, 5], [1, 2, 4, 5]) ➞ [1, 2, 4, 5]

common_elements([1, 2, 3, 4, 5], [10, 12, 13, 15]) ➞ []
Notes
Lists are sorted.
Try doing this problem with O(n + m) time complexity.
"""

def common_elements(lst1, lst2):

	return sorted(set(lst1) & set(lst2))

	# return [i for i in lst2 if i in lst1]

	# return sorted(list(set([i for i in lst1 if i in lst2])))

print(common_elements([-1, 3, 4, 6, 7, 9], [1, 3]))
print(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 3, 4, 7, 10]))
print(common_elements([1, 2, 2, 2, 3, 4, 5], [1, 2, 4, 5]))
print(common_elements([1, 2, 3, 4, 5], [10, 12, 13, 15]))
print(common_elements([18, 30, 60, 77, 89, 103, 107, 139, 149, 150, 201, 204, 233, 248, 250, 264, 273, 297, 308, 310, 319, 320, 348, 349, 353, 362, 365, 368, 376, 381, 395, 401, 405, 416, 421, 424, 434, 444, 452, 454, 464, 478, 497, 511, 513, 523, 533, 551, 562, 565, 593, 602, 604, 609, 610, 614, 620, 624, 643, 645, 654, 660, 674, 674, 685, 686, 700, 704, 712, 723, 728, 735, 741, 760, 765, 775, 776, 781, 787, 788, 791, 806, 823, 842, 848, 849, 901, 904, 909, 911, 916, 931, 932, 932, 940, 950, 951, 959, 973, 993], [3, 13, 25, 25, 27, 32, 39, 40, 45, 53, 55, 57, 60, 67, 78, 80, 81, 86, 114, 116, 125, 130, 146, 159, 164, 174, 192, 193, 209, 211, 265, 275, 279, 298, 303, 303, 314, 327, 330, 337, 355, 356, 375, 386, 405, 449, 452, 454, 457, 470, 476, 496, 499, 500, 501, 504, 516, 547, 577, 603, 604, 613, 618, 628, 638, 652, 659, 677, 683, 685, 700, 701, 710, 713, 727, 728, 734, 740, 774, 780, 790, 797, 833, 834, 837, 863, 869, 875, 885, 910, 911, 928, 930, 938, 943, 959, 964, 969, 987, 994]))

