"""
特定のスポーツ選手について、次の4つの引数を取るクラスを作成します。
①名前(name)、②年齢(age)、③身長(height)、④体重(weight)
また、次の文字列を返すクラス用に3つの関数を作成します。

get_age() returns "name of age"
get_height() returns "name of height (cm)"
get_weight() returns "name of weight (kg)"

例：
player1 = player('Patrick Mahomes', 24, 188, 104)
player2 = player('Jimmy Garoppolo', 28, 188, 102)
player3 = player('Julio Jones', 31, 191, 100)

player1.get_age() ➞ "David Jones is age 25"
player1.get_height() ➞ "David Jones is 175cm"
player1.get_weight() ➞ "David Jones weighs 75kg"

"""

class player():

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):

        return "{} is age {}".format(self.name, self.age)
        # return f"{self.name} is age {self.age}"

    def get_height(self):

        return "{} is {}cm".format(self.name, self.height)

    def get_weight(self):

        return "{} is {}kg".format(self.name, self.weight)


player1 = player('Patrick Mahomes', 24, 188, 104)
player2 = player('Jimmy Garaoppolo', 28, 188, 102)
player3 = player('Julio Jones', 31, 191, 100)

print(player1.get_age())
print(player1.get_height())
print(player1.get_weight())

print(player2.get_age())
print(player3.get_height())
print(player3.get_weight())





































# class player():
#
#     def __init__(self, name, age, height, weight):
#
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def get_age(self):
#
#         return "{} is age {}".format(self.name, self.age)
#         # return f"{self.name} is age {self.age}"
#
#     def get_height(self):
#
#         return "{} is {}cm".format(self.name, self.height)
#
#     def get_weight(self):
#
#         return "{} weighs {}kg".format(self.name, self.weight)
#
#
# player1 = player('Patrick Mahomes', 24, 188, 104)
# player2 = player('Jimmy Garoppolo', 28, 188, 102)
# player3 = player('Julio Jones', 31, 191, 100)
#
# print(player1.get_age())
# print(player1.get_height())
# print(player1.get_weight())
# print(player2.get_weight())
# print(player3.get_age())




