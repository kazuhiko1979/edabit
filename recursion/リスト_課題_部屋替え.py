"""
部屋替え
easy
Glover は定期的に部屋替えを行うルールがあるシェアハウスに住んでいます。くじ引きで数字をランダムに引いて、
その数だけ住人が部屋をずらす仕組みです（例：数字 2 を引いたとき、部屋番号 1 に住んでいる人は 3 に移動します）。
住人たちの ID をまとめた ids と、くじ引きで引いた自然数 n が与えられるので、住人の位置をずらさせた配列を返す、
rotateByTimes という関数を作成してください。

関数の入出力例

入力のデータ型： integer[] ids, integer n

出力のデータ型： integer[]

rotateByTimes([1,2,3,4,5],2) --> [4,5,1,2,3]

rotateByTimes([1,2,3,4,5],5) --> [1,2,3,4,5]

rotateByTimes([10,12,3,4,5],3) --> [3,4,5,10,12]

rotateByTimes([4,23,104,435,5002,3],26) --> [5002,3,4,23,104,435]

rotateByTimes([4,23,104,435,5002,3],0) --> [4,23,104,435,5002,3]

rotateByTimes([4,23,104,435,5002,3],1) --> [3,4,23,104,435,5002]

rotateByTimes([4,23,104,435,5002,3],2) --> [5002,3,4,23,104,435]

rotateByTimes([2,3],1) --> [3,2]
"""
# 時間計算量O(N)
# 空間計算量O(1)

import math

def reverseInPlace(arr, start, end):

    middle = math.floor((start + end) / 2)
    for i in range(start, middle + 1):
        opposite = start + (end - i)
        arr[i], arr[opposite] = arr[opposite], arr[i]

def rotateByTimes(ids, n):
    r = n % len(ids)
    if r == 0:
        return ids

    l = len(ids) - 1
    reverseInPlace(ids, 0, l)
    reverseInPlace(ids, 0, r-1)
    reverseInPlace(ids, r, l)

    return ids


    # # de = deque(ids)
    # # de.rotate(n)
    # # return de
    #
    # return np.roll(ids, 2)


print(rotateByTimes([1,2,3,4,5],2))
print(rotateByTimes([4,23,104,435,5002,3],26))


