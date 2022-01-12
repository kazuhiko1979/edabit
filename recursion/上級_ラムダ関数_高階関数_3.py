"""
高階関数(3)
では、次に関数を返すケースを見てみましょう。
このケースでは関数は入力を受け取り、複数の処理を行い、戻り値として呼び出し可能オブジェクトを生成します。
そして、この呼び出し可能オブジェクトは保存したり、実行したり、他の関数に渡したり、自由自在に操作をすることができます。
"""

def helloFunction():
    return lambda : 'hello world'


# この関数は関数を返します。
print(helloFunction())

# 戻り値としてこの関数を実行するか、保存することができます。
print(helloFunction()())
outputF = helloFunction()
print("Running a function that was generated.... " + outputF())

# 数値xを取り込み、その後xと入力を乗算する関数を返します。
def constantMultiplication(x):
    return lambda y: y * x

multiplyBy4 = constantMultiplication(4)
print(multiplyBy4(3))
print(multiplyBy4(10))
print(multiplyBy4(5))

# 惑星を表す文字列を受け取り、質量を受け取り、惑星の重量をニュートンで計算する関数を返します。
def weightFormulaByPlanet(planet):

    # 利用可能な惑星を検索します。デフォルトは地球です。
    planets = {
        "mercury": 3.7,
        "venus": 8.87,
        "earth": 9.807,
        "mars": 3.711,
        "jupiter": 24.79,
        "saturn": 10.44,
        "uranus": 8.87,
        "neptune": 11.15,
    }

    planet = planet.lower()
    if planets[planet] != None:
        gravity = planets[planet]
    else:
        gravity = planets["earth"]

    return lambda kgMass: kgMass * gravity

# 質量をkgを取り込み、地球上の質量をニュートンで返す関数を作成します。
getWeightEarth = weightFormulaByPlanet("earth")
print(getWeightEarth(50))
print(getWeightEarth(90))

getWeightJupiter = weightFormulaByPlanet("jupiter")
print(getWeightJupiter(50))
print(getWeightJupiter(90))

print(weightFormulaByPlanet('neptune')(50))

"""
最後に注意すべきことは、高階関数は必ずしも無名関数を入力として受け取る必要はないということです。
単純に関数への参照を渡すこともできます。 では、具体例を見てみましょう。
"""
import string
import random

def greeting(name):
    return "Hello there" + name

def nameGenerator():
    data = string.digits + string.ascii_lowercase
    return ''.join([random.choice(data) for _ in range(10)])

def multiCall(f, fInputF, message):
    return f(fInputF()) + '......' + message

print(multiCall(greeting, nameGenerator, "Thanks you"))













