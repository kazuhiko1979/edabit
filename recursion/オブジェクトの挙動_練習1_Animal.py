"""
練習1 - Animal
あなたは動物園で動物を研究するためのアプリを作っているチームに参加しています。
このアプリを通じて、動物園の参観者が動物の詳細を見ることができるようになることを計画しています。
以下に従って、動物の設計図を作成してください。
"""

class Animal:

    # どれほど動物が活発的か表す数字、動物園の動物は檻に入られているので、活動制限されているとみなし
    # 活動指数を1.2とします。
    activityMultiplier = 1.2

    def __init__(self, name, species, description, weightKg, heightM, \
                 isPredator, speedKph, urlPic, registerData):

        self.name = name # 動物の名前
        self.species = species # 動物の種
        self.description = description # 動物の説明
        self.weightKg = weightKg # 動物の体重kg
        self.heightM = heightM # 動物の身長（垂直に立ち上がった時の身長を指す）メートル
        self.isPredator = isPredator # 動物は捕食者かどうか
        self.speedKph = speedKph # 動物の時速
        self.urlPic = urlPic # 動物の写真のURL
        self.registerData = registerData # 動物園

        # 出力例1
        # rabbit.getStateString() : "name: rabbit, species: leporidae, description:
        # Rabbits are small mammals in the family Leporidae of the order Lagomorpha (along with the hare and the pika).,
        # weight: 10kg, height: 0.3m, Not Predator, speed: 20kph, urlPic: img1, registerDate: 2020/5/25"

    # 動物の情報を文字列として返します
    def getStateString(self):

        res_predator = "Predator, " if self.isPredator else "Not Predator, "

        return "name:" + str(self.name) + ", species:" + str(self.species) + ", description:" + \
        str(self.description) + " weight:" + str(self.weightKg) + "kg, " + "height:" + \
        str(self.heightM) + "m, " + res_predator + \
        "speed:" + str(self.speedKph) + "kph, " + "urlPic:" + str(self.urlPic) + \
        " registerDate:" + str(self.registerData)

    # 動物のBMIを返します。
    def getBmi(self):

        return self.weightKg / (self.heightM ** 2)

    # 動物の毎日カロリー消費量を返します。計算式：（70 * weight * ^0.75) * activityMultiplier
    def getDailyCalories(self):

        return (70 * self.weightKg ** 0.75) * self.activityMultiplier

    # // 動物が危険かどうか判断するブーリアン値を返します。動物が捕食者だった場合、危険とみなされ、
    # 身長が1.7メートル以上、もしくは時速35km/h以上の場合も危険とみなされます。
    def isDangerous(self):

        if self.isPredator == True or self.heightM >= 1.7 or self.speedKph >= 35:
            return True
        else:
            return False

    def isFaster(self, animal):
        # self.speedKph : elephant > animal.speedKph : rabbit
        return self.speedKph > animal.speedKph


rabbit = Animal("rabbit", "leporidae", "Rabbits are small mammals in the family Leporidae of the order Lagomorpha (along with the hare and the pika).", 10, 0.3, False, 20, "img1", "2020/5/25")
print(rabbit.getStateString())
print(rabbit.getBmi())
print(rabbit.getDailyCalories())
print(rabbit.isPredator)


elephant = Animal("elephant", "Elephantidae", "Elephants are mammals of the family Elephantidae and the largest existing land animals.", 300, 3, False, 5, "img2", "2020/5/26")
print(elephant.getStateString())
print(elephant.getBmi())
print(elephant.getDailyCalories())
print(elephant.isDangerous())
print(elephant.isFaster(rabbit))





