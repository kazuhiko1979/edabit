"""
ラムダ出力
ここまでは、ラムダ関数が入力として渡されたときの動作を見てきました。
ラムダ関数が出力として返される場合を見てみましょう。

関数を作って、それを高階関数の中で返すことができます。
もし、入力が何であっても常に返される関数が同じ場合、通常の関数を定義すればよいのですから、
この高階関数の処理は全く意味をなさないことになってしまいます。
"""

# この関数は通常の関数として定義すればよいので、これは無意味です。
# どのような入力であっても、常に同じ関数が返されます。

def lambdaHelloWorld(randomInput):
    print(randomInput + " was passed in but this function always \
     return the same lambda function")
    return lambda: 'Hello World'


def helloWorld():
    return 'Hello World'


# print(helloWorld())
# print((lambdaHelloWorld("laliluleko")()))


# Lambda Machine

import math
import random


class LambdaMachine:
    def __init__(self):
        self.lambdaStorage = []
        # バンドらはキーと値のペアを含み、キーは関数名、値は格納された
        # 関数のインデックスになります。ラムダ関数はこのlamdbaStorageに
        # 格納されます。
        self.handlers = {}
        self.counter = 0

    # キーに基づいて、ラムダ関数をデータ構造に挿入します。
    def insert(self, key, fLambda):
        if key in self.handlers:
            self.lambdaStorage[self.handlers[key]] = fLambda
            return
        else:
            self.lambdaStorage.append(fLambda)
            self.handlers[key] = len(self.lambdaStorage) - 1
    # 取得
    def retrive(self, key):
        if len(self.lambdaStorage) > 0 and key in self.handlers:
            return self.lambdaStorage[self.handlers[key]]
        else:
            None

    def roundRobinRetrieve(self):
        l = len(self.lambdaStorage)
        if l == 0:
            return None
        index = self.counter % l
        print("Round-Robin retrieval at index: " + str(index))
        self.counter += 1
        return self.lambdaStorage[index]

    def randomRetrieve(self):
        l = len(self.lambdaStorage)
        if l == 0:
            return None
        ran = math.floor(random.random() * l)
        print("Random retrieval at index: " + str(ran))
        return self.lambdaStorage[ran]


lambdaMachine = LambdaMachine()

# 2つの入力と共に、構造体ラムダに挿入します
lambdaMachine.insert("pythagora", lambda a, b: math.sqrt(a * a + b * b))
lambdaMachine.insert("addition", lambda x, y: x + y)
lambdaMachine.insert("subtraction", lambda x, y: x - y)
lambdaMachine.insert("multiplication", lambda x, y: x * y)
lambdaMachine.insert("division", lambda x, y: x / y)
lambdaMachine.insert("noises", lambda x, y: str(x) + "-DUM-DUM-DUM-DUM-" + str(y))

print(lambdaMachine.retrive("pythagora"))
print(lambdaMachine.retrive("pythagora")(3, 4))
print(lambdaMachine.retrive("multiplication"))
print(lambdaMachine.retrive("multiplication")(4, 10))
print(lambdaMachine.retrive("noises"))
print(lambdaMachine.retrive("noises")(10, 15))


x = 1
y = 10


print(lambdaMachine.randomRetrieve()(x, y))
print(lambdaMachine.randomRetrieve()(x, y))
print(lambdaMachine.randomRetrieve()(x, y))
print(lambdaMachine.randomRetrieve()(x, y))
print(lambdaMachine.randomRetrieve()(x, y))
print(lambdaMachine.randomRetrieve()(x, y))

# ラウンドロビンによる取得
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))













