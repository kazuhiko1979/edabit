"""
完全二分木の高さが
log2nであるという性質を利用して、O(logn) で検索できる構造を作成していきます。


では、まず探索について復習しましょう。中級「リスト：探索」のコンテンツで、O(n
) で干し草の山の中から針を見つける実装を行ったことを思い出しましょう。
"""

def linearSearch(key, haystack):
    for i in range(len(haystack)):
        if haystack[i] == key:
            return i
    return -1

l1 = [3, 4, 2, 5, 46, 23, 3, 55, 67, 24, 65]

print(linearSearch(5, l1))
print(linearSearch(24, l1))


