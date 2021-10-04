"""
長方形を定義します。長方形とはそれぞれの内角が 90° で、対辺が平行な 2 次元の図形のことを指します。
したがって、設計図であるクラスを使って、この性質をデータとして表現することができます。
double 型の高さと幅の値をそれぞれ使うことによって、各長方形オブジェクトを表してみましょう。
またオブジェクトの情報を文字列で返すメソッドも作成します。
"""

class Rectangle:
    # init関数は、オブジェクトの初期値のデータ、および状態を作成します。
    # selfパラメータはメモリから現在のオブジェクトを取得します。
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def getRecangleString(self):
        return "The recangle has a width of: " + str(self.width) \
               + " and a height of: " + str(self.height)






# rectangle1 = Rectangle(20, 100)
# print(rectangle1.getRecangleString())
#
# rectangle2 = Rectangle(46, 30)
# print(rectangle2.getRecangleString())
#
# square1 = Rectangle(20, 20)
# print(rectangle2.getRecangleString())

"""
車の設計図を作成し、いくつかの車のオブジェクトを作成してみましょう。
車の情報を文字列として表すメソッドも作成します。"""

class Car:
    # Pythonでは、__init__コンストラクタ関数です。
    # オブジェクトが作られる際、最初にコンストラクタが実行されます。
    # オブジェクトの初期状態を設定します。

    # クラス変数を作成します。全てのオブジェクトはクラス変数を持ちます。
    wheels = 4
    """
    Pythonではメモリから現在のオブジェクトを取得します。これは最初のパラメータで、残りのパラメータは
    関数呼び出しから渡された通常のパラメータです。
    メンバ変数には「.」によって、アクセスすることができます。
    各オブジェクトはそれぞれスコープを持っています。したがって、Pythonではメンバ変数にアクセスすることにより
    任意の場所で変数を作ることができます。
    もしメンバ変数が存在しない場合は、それを作成し、もし存在する場合は、それを取得します。
    """

    def __init__(self, make, model, year, vin, color, velocity, fuelEconomy,
                 tankCapacity, weightKg):
        """
        コンストラクタは、
        :param make:
        :param model:
        :param year:
        :param vin:
        :param color:
        のそれぞれの値を入力として受け取ります。
        これらの入力のそれぞれに対して、メンバ変数を割り当てます。これはオブジェクトの最初の状態になります。
        """
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.color = color
        self.velocity = velocity # 速度
        self.fuelEconomy = fuelEconomy
        self.tankCapacity = tankCapacity
        self.weightKg = weightKg

    # 車の情報を文字列として返します。
    def getCarString(self):
        return self.make + " " + self.model + " " + str(self.year) + " " + \
               self.vin + " " + self.color + "Velocity: " + str(self.velocity) + \
            "mps Fuel economy: " + str(self.fuelEconomy) + "mile/gallon Tank capacity: " + \
            str(self.tankCapacity) + " Weigth: " + str(self.weightKg) + \
               ". It has " + str(Car.wheels) + " wheels."

    """
    新しい車のオブジェクトを作成します。Pythonではクラス名（コンストラクタの入力）によって作成されます。
    これはクラス名のオブジェクトを返します。
    新しいオブジェクトが作成されました。最初の状態はmake="tesla", model="Model S", year=2013, vin = "***", color="Black
    今、teslaSにはメモリアドレスが保存されています
    """

    def milesWithoutStop(self):
        # 停止せずに移動ができる最大マイル数

        return self.fuelEconomy * self.tankCapacity

    def getDistance(self):
        # 1時間ごとに進むことができる距離（燃費）
        return self.velocity * 60 * 60

    def hoursToEmpty(self):
        # ガソリンが空になるのに何時間かかるか（7.4、5.6時間のように小数点第2以下は切り捨ててください）
        return round(self.milesWithoutStop() / self.getDistance())


    def getEnergy(self):
        # 車が持つ運動エネルギー
        return (self.velocity ** 2) * self.weightKg / 2


# teslaSの状態を出力します。
# getCarString()　メソッドはteslaSの情報を文字列として表します。

# teslaS.color = "white"
# print(teslaS.getCarString())
#

# print(pursche88.getCarString())
#
# ferrari08 = Car("Ferrari", "F430 Spyder", 2008, "ZFFEZ59E780163510", "Orange")
# print(ferrari08.getCarString())
# ferrari08.vin = "WB10228019ZT94950"
# print(ferrari08.getCarString())
#
# Car.wheels = 5
# print()
# print(teslaS.getCarString())
# print(pursche88.getCarString())
# print(ferrari08.getCarString())
teslaS = Car("Tesla", "Model S", 2013, "SYJSA1CN0DFP13393", "Black", 0.04, 98, 12, 2162)
print(teslaS.getCarString())
print(teslaS.milesWithoutStop())
print(teslaS.getDistance())
print(teslaS.hoursToEmpty())
print(teslaS.getEnergy())

porsche88 = Car("Porsche", "928", 1988, "WP0JB0926JS861742", "Red", 0.057, 36, 12, 1390)
print(porsche88.getCarString())
print(porsche88.getCarString())
print(porsche88.milesWithoutStop())
print(porsche88.getDistance())
print(porsche88.hoursToEmpty())
print(porsche88.getEnergy())

ferrari08 = Car("Ferrari", "F430 Spyder", 2008, "ZFFEZ59E780163510", "Orange", 0.059, 11, 18, 1570)

print(ferrari08.getCarString())
print(ferrari08.milesWithoutStop())
print(ferrari08.getDistance())
print(ferrari08.hoursToEmpty())
print(ferrari08.getEnergy())










