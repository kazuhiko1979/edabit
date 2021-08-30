def isEven(n):

    return "The number " + str(n) + " is even" if n % 2 == 0 \
        else "The number " + str(n) + " is odd"

# Pythonでは、三項演算子は以下のようになります。
# (条件がTrueの時の値）if (条件）else (条件がFalseの時の値）

# print(isEven(43))
# print(isEven(44))
# print(isEven(1023))
# print(isEven(9992))

"""
# 例題1
# アルファベットが与えられるので、文字コードが奇数の時にTrue、
偶数の時にFalseを返す、isEncodeOddという関数を作成してください。
# "a" -> True
# "k" -> True
# "p" -> False
# "z" -> False
"""

def isEncodeOdd(str):

    return ord(str) % 2 != 0

# print(isEncodeOdd("a"))
# print(isEncodeOdd("k"))
# print(isEncodeOdd("p"))
# print(isEncodeOdd("z"))


"""
# 例題2
# ビットが与えられるので、0と1を反転するoneComplementという関数を再帰を使って作成してください。

# "0101010" -> "1010101"
# "0000" -> "1111"
# "111111" -> "000000"
# "1011110" -> "0100001"
"""


def oneComplement(str, count=0):

    lst_str = list(str)

    if count < int(len(str)):

        if str[count] == "1":
            lst_str[count] = "0"
        elif str[count] == "0":
            lst_str[count] = "1"

        return oneComplement(lst_str, count+1)

    return ''.join(lst_str)

# print(oneComplement("0101010"))
# print(oneComplement("0000"))
# print(oneComplement("111111"))
# print(oneComplement("1011110"))


def monsterAttackExpressionNest(monster):

    attack = 1000
    message = "'s attack is:"

    # モンスターの名前を入力として受け取って、ケースで比較してみましょう。
    # 入れ子構造
    return "Cyclops" + message + str(attack * 1.8) if monster == "Cyclops" \
        else "Ogre" + message + str(attack * 2.5) if monster == "Ogre" \
        else "Zombie" + message + str(attack * 1.2) \
        if monster == "Zombie" else "Monster does not exist."

# print(monsterAttackExpressionNest("Cyclops"))
# print(monsterAttackExpressionNest("Ogre"))
# print(monsterAttackExpressionNest("Zombie"))
# print(monsterAttackExpressionNest("Ghost"))


def redirectionUrl(lang):

    url = "www.example.org/"
    return url + "en" if lang == "English" \
        else url + "ja" if lang == "Japanese" \
        else url + "es" if lang == "Spanish" \
        else url + "ru" if lang == "Russian" \
        else url

print(redirectionUrl("English"))
print(redirectionUrl("Japanese"))
print(redirectionUrl("Spanish"))
print(redirectionUrl("Russian"))
print(redirectionUrl("China"))















