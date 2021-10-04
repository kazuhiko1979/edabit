"""
オブジェクトの状態と配列
配列とオブジェクトのデータ型に慣れるために、オブジェクトの配列が必要なシミュレーションを作成します。
今回はハンティングゲームを考えてみます。このゲームのハンターは、檻を使って野生の動物を捕獲しようとしています。
ハンターはオブジェクトとして表現され、強さと檻の大きさを数値として持っています。
ハンターの強さと檻の大きさによって、捕獲できる動物、飼い慣らすことができる動物が決まります。

動物もオブジェクトの状態として表され、その状態として、種、体重、身長、捕食者であるかどうかが含まれています。
ハンターが動物よりもはるかに強ければ、動物を飼い慣らすことができるとします。
captureAnimals という関数は、動物のリストとハンターを受け取り、捕獲可能な動物だけを返します。
ハンターが捕獲できるのは、動物がハンターの持っている檻のサイズより小さく、さらに捕食者でない場合に限ります。
では、まずは動物のデータ構造、動物の状態を表示する関数を作成しましょう。
"""

# ハンターをオブジェクトとして表現
# ハンターは動物を捕獲できるかどうか判断することができます。
# ハンターは動物を飼い慣らすことができます。

class Hunter:
    def __init__(self, name, age, weightKg, heightM, strength, cageCubicMeters):
        self.name = name
        self.age = age
        self.weightKg = weightKg
        self.heightM = heightM
        # strengthは体重と掛け算され、ハンターの強さを表します。
        self.strength = strength
        self.cageCubicMeters = cageCubicMeters

    def canCaptureAnimal(self, animal):
        # ハンターが動物を運べて、かつ檻の大きさより動物が小さい場合、動物は捕獲されます。
        # また、動物は捕食者でない必要があります。
        return True if self.strengthKg() >= animal.weightKg and \
                       self.cageCubicMeters >= animal.heightM and not animal.predator else False


    # 動物を飼い慣らします。
    # ハンターが動物の体重より2倍以上重ければ、その動物を飼い慣らすことができます。
    def attemptToDomesticate(self, animal):
        if self.strengthKg() <= animal.weightKg * 2:
            return False
        # 動物のステータスを変更します。
        animal.domesticate()
        return True

    # ハンターの強さを決定します。
    def strengthKg(self):
        return self.weightKg * self.strength


def printHunter(hunter):
    print("The hunter's name is: " + hunter.name + ". This hunter can carry: " +
          str(hunter.strengthKg()) + "kg and has a cage " + str(hunter.cageCubicMeters) +
          " cubic meters wide")


# 動物をオブジェクトして表現しましょう
class Animal:
    def __init__(self, species, weightKg, heightM, predator):
        self.species = species
        self.weightKg = weightKg
        # 動物が立ち上げることを仮定すると、高さは最大の寸法になります。
        self.heightM = heightM
        self.predator = predator

    # 捕食者かどうかの状態を変更します。
    def domesticate(self):
        self.predator = False

def printAnimal(animal):
    print("The animal species is: " + animal.species +
          ". It's weight is: " + str(animal.weightKg) +
          "kg and its height is: " + str(animal.heightM) +
          "m. " +
          "It is a predator!" if animal.predator else "It is a peaceful animal.")

# 捕まえた動物を返す関数
def capturedAnimals(hunter, animalList):
    capturedAnimalList = []
    for i in range(len(animalList)):
        # もし、ハンターが動物を捕獲した場合、配列の後ろに追加します。
        if hunter.canCaptureAnimal(animalList[i]):
            print("Capturing..." + animalList[i].species)
            capturedAnimalList.append(animalList[i])
    return capturedAnimalList

def printAnimals(animalList):
    print("----Listing Animals----")
    # それぞれの動物にアクセスするために異なる構文のfor文を使います。
    # 各 animalList をループします。それぞれの値は "currentAnimal"の一時変数に直接渡されます。

    for currentAnimal in animalList:
        # 動物を出力します。
        printAnimal(currentAnimal)
    print("------------------------")


# 各動物
tiger1 = Animal("Tiger", 290, 2.6, True)
tiger2 = Animal("Tiger", 300, 2.3, True)
bear1 = Animal("Bear", 250, 2.8, True)
snake1 = Animal("Snake", 250, 12.8, True)
dog1 = Animal("Dog", 90, 1.2, False)
cat1 = Animal("Cat", 40, 0.5, False)
cow1 = Animal("Cow", 1134, 1.5, False)

# 各ハンター
hunternator = Hunter("Hunternator", 30, 124.73, 1.85, 15, 3)
hunterChild = Hunter("Hunter Child of The Small Ginants", 10, 50, 1.2, 0.6, 1)

# 関数の呼び出し
printHunter(hunternator)

animals = [tiger1, tiger2, bear1, snake1, dog1, cat1, cow1]
print("Animals in the wild: ")
printAnimals(animals)

print("Animals captured by: " + hunternator.name + "")
printAnimals(capturedAnimals(hunternator, animals))

print("" + hunternator.name + " is ready to bring peace to the animal kingdom")

# ハンターと動物のリストを受け取り、動物の状態を変更します。
# つまりハンターが動物より圧倒的に強ければ、飼い慣らされます。

def domesticateTheAnimals(hunter, animalList):
    # for文でリストをループし、動物を飼い慣らす関数を呼び出します。
    for i in range(0, len(animalList)):
        hunter.attemptToDomesticate(animalList[i])

domesticateTheAnimals(hunternator, animals)
print("Animals captured by: " + hunternator.name + "")
printAnimals(capturedAnimals(hunternator, animals))








