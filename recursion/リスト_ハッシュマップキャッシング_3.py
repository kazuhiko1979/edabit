"""
ハッシュマップは、O(n) メモリの使用が許容される限り、ルックアップが必要な一般的なアルゴリズムのキャッシングに使用することができます。
実際、メモリを節約するために使われることもあります。

例えば、重複を含む要素のリストを考えてみましょう。ハッシュマップを使って、
要素の集合をキーとして格納し、その値の個数を値として格納してみましょう。

任意のリストを受け取り、リストの集合要素と、その要素の個数を示す文字列のシーケンスを出力する関数を作成してみましょう。
"""
def printDuplicates(inputList):
    hashmap = {}

    for i in range(int(len(inputList))):

        # hashmap[str(inputList[i])] = 1 if str(inputList[i]) not in hashmap else hashmap[str(inputList[i])] + 1

        if str(inputList[i]) in hashmap:
            hashmap[str(inputList[i])] += 1
        else:
            hashmap[str(inputList[i])] = 1
    keys = list(hashmap.keys())
    print(keys)

    # dictionary.items()を利用して、キーと値の両方を取得します。
    # items()の戻り値はtupleの配列です[[key, value]], [[key, value]], [key, value].....

    for (key, value) in hashmap.items():
        print(key + " has " + str(value) + " duplicates.")

# printDuplicates([1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,5,6,6,6,6,7,8,8,8,9,9,9])
# printDuplicates([7,7,6,6,3,5,3,9,2,5,5,4,6,4,1,4,1,7,2])

# 例題1
# アルファベットで構成される文字列が与えられるのでそれがパングラムかどうか判定する、isPangramという関数を作成してください。パングラムとは、a-zまでの全てのアルファベットを含んだ文字列のことを指します。

# "we promptly judged antique ivory buckles for the next prize" -> true
# "sheep for a unique zebra when quick red vixens jump over the yacht" -> false
# "a quick brown fox jumps over the lazy dog" -> true

def isPangram(string):

    hashmap = {}
    for i in string.replace(" ", "").lower():
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
    if len(hashmap) == 26:
        return "True"
    else:
        return "False"

# True
# print(isPangram("we promptly judged antique ivory buckles for the next prize"))
#
# # False
# print(isPangram("sheep for a unique zebra when quick red vixens jump over the yacht"))
#
# # True
# print(isPangram("a quick brown fox jumps over the lazy dog"))


# 例題2
# 文字列stringが与えられるので、全ての文字が同じ数だけ含まれているかどうか判定するfindXTimesという関数を作成してください。
def findXTimes(string):
    hashmap = {}

    for i in string:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
    # return hashmap
    count = 0
    initial = hashmap[string[0]]
    # print(initial)

    for key, value in hashmap.items():
        if value == initial:
            count += 1
    if count == len(hashmap):
        return True
    return False





# True
print(findXTimes("babacddc"))

# True
print(findXTimes("aaabbbcccddd"))

# False
print(findXTimes("aaabbccdd"))

# True
print(findXTimes("zadbchvwxbwhdxvcza"))

# False
print(findXTimes("zadbchvwxbwhdxvczb"))