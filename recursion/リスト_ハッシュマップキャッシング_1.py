"""
ハッシュマップの平均時間計算量は O(1) です。この機能のおかげで、ハッシュ関数が使われている限り、
私たちはすべてのプログラミング言語でキーに基づいたリスト内のデータを一定時間で取得することができます。
"""

def existsWidthinList(listL, dataY):

    hash_map = {}
    for i in range(int(len(listL))):
        hash_map[str(listL[i])] = listL[i]
    return False if hash_map.get(str(dataY)) is None else True

sampleList =  [3,10,23,3,4,50,2,3,4,18,6,1,-2]

# print(existsWidthinList(sampleList, 23))
# print(existsWidthinList(sampleList, -2))
# print(existsWidthinList(sampleList, 100))


"""
# TODO: リストと値を受け取り、リスト内にある値のインデックスを返す、
searchListという関数をハッシュマップを使って作成してください。
値がリスト内に複数ある場合は先に出てきたインデックスを返してください。
もし発見されない場合は-1を返してください。
"""

def searchList(givenList, value):

    hashMap = {}

    for i in range(len(givenList)):
        if hashMap.get(givenList[i]) is not None:
            continue
        hashMap[givenList[i]] = i
    return hashMap.get(value) if hashMap.get(value) is not None else -1

    #     hashMap[str(givenList[i])] = givenList[i]
    # return -1 if hashMap.get(str(value)) is None else givenList.index(value)


sampleList =  [3,10,23,3,4,50,2,3,4,18,6,1,-2]

print(searchList(sampleList, 23))
print(searchList(sampleList,-2))
print(searchList(sampleList,100))

