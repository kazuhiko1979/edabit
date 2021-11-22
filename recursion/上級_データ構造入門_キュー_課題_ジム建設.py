"""
ジム建設
hard
あなたは今ジムの建設チームのエンジニアです。今連結したビルのような建物の中にジムを建設しようとしています。高さを表す配列 h がヒストグラムとして与えられるので、ヒストグラム内に描くことのできる長方形の最大面積を返す、largestRectangle という関数を作成してください。


関数の入出力例

入力のデータ型： integer[] h

出力のデータ型： integer

largestRectangle([3,2,3]) --> 6

largestRectangle([1,2,5,2,3,4]) --> 10

largestRectangle([1,2,3,4,5]) --> 9

largestRectangle([3,4,5,8,10,2,1,3,9]) --> 16

largestRectangle([1,2,1,3,5,2,3,4]) --> 10

largestRectangle([11,11,10,10,10]) --> 50

largestRectangle([8979,4570,6436,5083,7780,3269,5400,7579,2324,2116]) --> 26152

この問題は難しいのでまずは計算量を気にせずに解いてみましょう。
for文で高さの配列をループしながら、その時作れる長方形の面積を配列で記録し、
できた配列の中から最大値を探します。現在の要素を高さとすると、長方形の面積を出すために横の長さを決めなければいけません。
現在の要素から左右の要素へと高さを比較し、現在の要素よりも高いか同じ時は横幅に1足していきます。

計算量を減らし効率のいいコードにするため、スタックを使ってO(n)で解いてみましょう。
"""

# def stackCounter(arr):
#     # Contains indexs
#     stack = []
#     results = [0] * len(arr)
#     i = 0
#     for x in arr:
#         total = 1
#         while len(stack) != 0 and arr[stack[-1]] >= x:
#             j = stack.pop()
#             total += results[j]
#
#         stack.append(i)
#         results[i] = total
#         i += 1
#
#     return results
#
# def largestRectangle(h):

    # left = stackCounter(h)
    # right = stackCounter(h[::-1])[::-1]
    # total = [(left[i] + right[i] - 1) * h[i] for i in range(len(h))]
    #
    # return max(total)


# def largestRectangle(h):
#
#     squreList = []
#     for i in range(len(h)):
#         currH = h[i]
#         # print(currH)
#         width = 0
#         for j in range(len(h)):
#             width = 0 if currH > h[j] else width + 1
#             squreList.append(currH * width)
#         print(squreList)



# 連続した高さの最大幅を返す
# def consecuteNumbrer(arr, th):
#     count = 0
#     max_count = 0
#
#     for h in arr:
#         if h < th:
#             if count > max_count:
#                 max_count = count
#             count = 0
#         else:
#             count = count + 1
#
#     if count > max_count:
#         return count
#     else:
#         return max_count
#
# def largestRectangle(h):
#     area_max = 0
#
#     for height in sorted(h):
#         area = height * consecuteNumbrer(h, height)
#         if area_max < area:
#             area_max = area
#     return area_max
#

# def largestRectangle(h):
    # results = [0] * (len(h))
    # # nested for loops, O(n)
    #
    # for i in range(len(h)):
    #     j = i - 1
    #     total = 1
    #     curr = h[i]
    #     while j >= 0 and curr <= h[j]:
    #         total +=1
    #         j -= 1
    #     j = i + 1
    #     while j < len(h) and curr <= h[j]:
    #         total += 1
    #         j += 1
    #     results[i] = total*curr
    #
    # return max(results)


# stack, insert(1), delete(1), LIFO
# dynamic array

def stackCounter(arr):
    stack = []
    results = [0] * len(arr)
    i = 0
    for x in arr:
        total = 1
        while len(stack) != 0 and arr[stack[-1]] >= x:
            j = stack.pop()
            total += results[j]

        stack.append(i)
        results[i] = total
        i += 1

    return results

def largestRectangle(h):

    left = stackCounter(h)
    right = stackCounter(h[::-1])[::-1]

    total = [(left[i]+right[i]-1) * h[i] for i in range(len(h))]
    return max(total)

# ith
# 0, 1, 2, 3, 4, 5 index
# [1,2,1,3,5,2,3,4] value

# left [1,1,
# value [1,2,1
# index [0,1,2

# right []
# value [
# right [


# print(largestRectangle([1,2,5,2,3,4]))
# print(largestRectangle([1,2,3,4,5]))
print(largestRectangle([1,2,1,3,5,2,3,4]))


