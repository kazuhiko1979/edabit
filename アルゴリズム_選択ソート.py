# 選択ソート
def select_sort(arr):
	for i in range(0, len(arr) -1):
		select_min(arr, i)

def select_min(arr, i):
	# 最小要素の位置の特定
	min = i
	for j in range(i+1, len(arr)):
		if arr[min] > arr[j]:
			min = j
	# 最小要素と先頭要素を交換
	arr[i], arr[min] = arr[min], arr[i]


	# temp = []
	# temp.append(lst[0])
	#
	# for i in range(1, len(lst)):
	# 	if temp[-1] > i:
	# 		temp.insert(0, i)
	# 	elif temp[-1] == i:
	# 		pass
	# 	else:
	# 		temp.append(i)
	# return temp

# 挿入ソート
def insert_sort(arr):
	for i in range(1, len(arr)):
		insert(arr, i)

def insert(arr, i):
	tmp = arr[i] # 未ソート要素の先頭を一時的な(tmp) 変数に代数
	for j in range(i - 1, -1, -1):
		if tmp < arr[j]:
			arr[j+1] = arr[j]
		else:
			arr[j+1] = tmp
			break
	else:
		arr[0] = tmp


# バブルソート
def bubble_sort(arr):
	for i in range(0, len(arr)-1):
		exchange(arr, i)

def exchange(arr, i):
	for j in range(len(arr)-1, i, -1): #リストの末尾から順番に
		if arr[j-1] > arr[j]: #要素を比較して大小関係が逆なら
			arr[j-1], arr[j] = arr[j], arr[j-1] #位置を交換する

org_list = [2,5,1,4,6,3]
select_sort(org_list)
print(org_list)
insert_sort(org_list)
print(org_list)
bubble_sort(org_list)
print(org_list)


