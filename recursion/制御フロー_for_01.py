# Range(min, max)は、min <= i < max の間のすべての数値リストを
# 生成します。
# iは一時的な変数なので、ループが実行されるとこの変数はリストにおける
# 現在の値になります。

def countUpToN(n):
    for i in range(0, n+1):
        print(i)

def printAllCharacters(inputString):
    for i in range(0, len(inputString)):
        print(inputString[i])


def printAllCharactersAlt(string):
    for i in string:
        print(i)


# countUpToN(15)
# printAllCharacters("Hello world!!")
# printAllCharactersAlt("Hello")


def printFizzbuzz(num):

    if num % 15 == 0:
        print("fizzbuzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
    else:
        print(num)

printFizzbuzz(15)
printFizzbuzz(30)
printFizzbuzz(12)
printFizzbuzz(25)
printFizzbuzz(18)
printFizzbuzz(11)
