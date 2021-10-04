
# ref: https://mobile.twitter.com/search?q=%23recursionCS%20%E9%96%93%E3%81%AE&src=typed_query&f=top

# ref: https://recursionist.io/dashboard/problems/submissions/108042

# Python
# ref: https://recursionist.io/dashboard/problems/submissions/38279

"""
間のアルファベット
easy
Sam は a駅、b駅、...y駅、z駅とアルファベットが各駅の名前になっている路線の電車に乗っています。]
Sam は自分が乗った駅から降りる駅まで、全ての停止場所を確認しました。
乗車駅 firstAlphabet、降車駅 secondAlphabet が与えられるので、停止駅を配列として返す、
generateAlphabet という関数を定義してください。
ただし、アルファベットは大文字と小文字を区別せず、全て小文字で表示し、a に近い文字から返すようにしてください。

関数の入出力例

入力のデータ型： char firstAlphabet, char secondAlphabet

出力のデータ型： char[]

generateAlphabet("a","z") --> [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

generateAlphabet("b","b") --> [b]

generateAlphabet("C","Z") --> [c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

generateAlphabet("M","z") --> [m,n,o,p,q,r,s,t,u,v,w,x,y,z]

generateAlphabet("z","a") --> [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
"""

def generateAlphabet(firstAlphabet,secondAlphabet):


    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', \
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    res = []

    if ord(firstAlphabet.lower()) > ord(secondAlphabet.lower()):
        firstAlphabet, secondAlphabet = secondAlphabet, firstAlphabet
        for i in range(ord(firstAlphabet.lower()), ord(secondAlphabet.lower()) + 1):
            res.append(chr(i))
    else:
        for i in range(ord(firstAlphabet.lower()), ord(secondAlphabet.lower()) + 1):
            res.append(chr(i))
    return res

    # if ord(firstAlphabet.lower()) > ord(secondAlphabet.lower()):
    #     firstAlphabet, secondAlphabet = secondAlphabet, firstAlphabet
    #     # ascii_Code = [chr(i) for i in range(ord(firstAlphabet.lower()), ord(secondAlphabet.lower()) + 1)]
    #     for i in range(ord(firstAlphabet.lower()), ord(secondAlphabet.lower()) + 1):
    #         res += ','.join(chr(i))
    # else:
    #     for i in range(ord(firstAlphabet.lower()), ord(secondAlphabet.lower()) + 1):
    #         res += ','.join(chr(i))
    # print(list(res))


# 回答例
def generateAlphabet(firstAlphabet, secondAlphabet):
    # 各文字を小文字に変えます
    first = firstAlphabet.lower()
    second = secondAlphabet.lower()

    # 各文字を文字コードに変換し、どちらがaに近い文字か判別します。
    # 値が小さい方がaに近くなります。
    if ord(first) > ord(second):
        smaller = ord(second)
    else:
        smaller = ord(first)

    if ord(first) < ord(second):
        larger = ord(second)
    else:
        larger = ord(first)

    res = []

    # aに近い文字から順に配列へ格納していきます
    for i in range(smaller, larger+1):
        # 文字コードを文字へ変換して、配列に格納します
        res.append(chr(i))

    return res

print(generateAlphabet("a","z"))
print(generateAlphabet("b","b"))
print(generateAlphabet("C","Z"))
print(generateAlphabet("M","z"))
print(generateAlphabet("z","a"))














