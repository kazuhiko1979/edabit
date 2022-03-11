"""
リストと集合が与えられたとき、その項目を昇順に並べたリストを返す。
ただし、集合の要素をリストの他の項目より優先する。

例
priority_sort([5, 4, 3, 2, 1], {2, 3}) ➞ [2, 3, 1, 4, 5] とする。

priority_sort([5, 4, 3, 2, 1], {3, 6}) ➞ [3, 1, 2, 4, 5] となります。

priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}) ➞ [-4, -3, -5, -2, -1, 0] となります。

"""

def priority_sort_v1(lst, s):

	# v1
	if lst:
		hi = sorted([x for x in lst if x in s])
		# print(hi)
		normal = sorted([j for j in lst if j not in hi])
		# print(normal)
	return hi + normal

def priority_sort_v2(lst, s):

	beg = []
	for x in s:
		while x in lst:
			lst.remove(x)
			beg.append(x)
	return sorted(beg) + sorted(lst)

def priority_sort_v3(lst, s):

	return sorted(lst, key= lambda x: (x not in s, x))



if __name__ == '__main__':
	print(priority_sort_v1([5, 4, 3, 2, 1], {2, 3}))
	print(priority_sort_v2([5, 4, 3, 2, 1], {2, 3}))
	print(priority_sort_v3([5, 4, 3, 2, 1], {2, 3}))
	print(priority_sort_v1([5, 4, 3, 2, 1], {3, 6}))
	print(priority_sort_v2([5, 4, 3, 2, 1], {3, 6}))
	print(priority_sort_v3([5, 4, 3, 2, 1], {3, 6}))








