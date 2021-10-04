"""
あなたは今コミュニティサイエンスプロジェクトのアプリケーションを作成しています。
このプロジェクトでは汎用的に惑星を表現する必要があります。以下の構造に沿った惑星の設計図を作成してください。
少し物理の内容が入るので、物理が苦手な方は解けなくても全く問題ありません。
"""
"""
# 状態
String name: 惑星の名前
double massKg: 惑星の質量
double meanRadiusKm: 惑星の半径
double distanceToStarLs: 惑星系システム内で、惑星から恒星まで光が届くのにかかる時間(s)。
太陽系の惑星が太陽(恒星)の周りを回っているように、惑星系とは恒星の重力により結合され、複数の天体が公転している構造のことを指します。

# 状態 - クラス変数
double constantOfGravitation: // 万有引力定数。6.67438 * 10−11 を使用してください。
double speedOfLight:// 光速(m/s)。2.99792458 * 10-8 を使用してください。
double massOfSun:// 太陽の質量(kg)。 1.989 * 10-30 を使用してください。
double radiusOfSun:// 太陽の半径(km)。　6.96 * 10-5 を使用してください。
int OneYear:// 1年(sec)。　1年間は31556926秒

# 挙動
double getVolume(): // 惑星の体積を返します。球体の体積を求める公式を使ってください。
double getSurfaceArea(): // 惑星の表面積を返します。
double compareToPlanet(planet): // 入力から渡される惑星と比較して、惑星の体積の差を表すスカラ値を返します。
double getSurfaceGravity(): // 惑星の重力を返します。(惑星の質量×万有引力定数/惑星の半径の2乗を使って求めてください
double getDistanceToStarKm(): 公転半径(km)を返します。公転距離とは惑星から恒星までの距離のことを指します。
double getOrbitalSpeed(): // 公転速度(m/s）を返します。太陽の質量は各惑星の質量に比べて非常に大きいので、惑星は太陽の周りを
円運動していると仮定してください。また遠心力と引力が等しいとして計算してください。
double getOrbitalPeriodYear(): // 公転周期（year)を返します。
"""
import math

class Planet:

    constantOfGravitation = 6.67438e-11 # 万有引力定数
    speedOfLight = 2.99792458e8 # 光速[m/s]
    massOfSun = 1.989e30 # 太陽の質量[kg]
    radiusOfSun = 6.96e5 # 太陽の半径[km]
    oneYear = 31556926 # 1年[sec]

    def __init__(self, name, massKg, meanRadiusKm, distanceToStarLs):
        self.name = name
        self.massKg = massKg
        self.meanRadiusKm = meanRadiusKm
        self.distanceToStartLs = distanceToStarLs

    # 惑星の体積(4/3πr^3)
    def getVolume(self):

        return 4 / 3 * math.pi * self.meanRadiusKm ** 3

    # 惑星の表面積(4πr^2)
    def getSurfaceArea(self):

        return 4 * math.pi * self.meanRadiusKm ** 2

    # 入力から渡される惑星と比較して、惑星の体積の差を表すスカラ値を返します。
    def compareToPlanet(self, planet):

        return math.fabs(self.getVolume() - planet.getVolume())

    # 惑星の重力を返します。(惑星の質量×万有引力定数/惑星の半径の2乗を使って求めてください
    def getSurfaceGravity(self):

        return self.massKg * Planet.constantOfGravitation / (self.meanRadiusKm * 1000) ** 2

    # 公転半径: 公転距離とは惑星から恒星までの距離のことを指します。
    def getDistanceToStarKm(self):

        return self.distanceToStartLs * self.speedOfLight / 1000

    # 公転速度(m / s）を返します。
    # 遠心力と引力が等しい速度（第一宇宙速度）として計算します。
    # (太陽の質量 × 万有引力 / 公転反転) ** 0.5
    def getOrbitalSpeed(self):

        return (Planet.massOfSun * Planet.constantOfGravitation /
                (self.getDistanceToStarKm() * 1000)) ** 0.5

    # 公転周期[year](2πR/V)
    # (2×円周率*公転半径)/公転速度
    def getOrbitalPeriodYear(self):

        getorbitalPeriodSec = self.getDistanceToStarKm() * 1000 * 2 * math.pi / self.getOrbitalSpeed()

        return getorbitalPeriodSec / Planet.oneYear


mercury = Planet("Mercury", 3.302e23, 2.4397e3, 1.931e2)
venus = Planet("Venus",4.869e24, 6.0518e3, 3.602e2)
earth = Planet("Earth", 5.974e24, 6.3782e3, 4.990e2)
mars = Planet("Mars", 6.419e23, 3.3972e3, 7.602e2)
jupiter = Planet("Jupiter", 1.899e27, 7.1492e4, 2.596e3)
saturn = Planet("Saturn", 5.6880e26, 6.0268e4, 4.760e3)
uranus = Planet("Uranus", 8.6830e25, 2.5559e4, 9.57e3)
neptune = Planet("Neptune", 1.0240e26, 2.4786e04, 15e3)


# 出力例
# earth.getOrbitalPeriodYear() : 0.999871509268352
# saturn.getOrbitalPeriodYear() : 29.458037062791014
# earth.getSurfaceGravity() : 9.801214211045128


print("-----Earth-----")
# print(earth.getVolume())
# print(earth.getSurfaceArea())
# print(earth.compareToPlanet(saturn))
print(earth.getSurfaceGravity())
# print(earth.getDistanceToStarKm())
# print(earth.getOrbitalSpeed())
print(earth.getOrbitalPeriodYear())

print("-----saturn-----")
# print(saturn.getVolume())
# print(saturn.getSurfaceArea())
# print(saturn.compareToPlanet(saturn))
# print(saturn.getSurfaceGravity())
# print(saturn.getDistanceToStarKm())
# print(saturn.getOrbitalSpeed())
print(saturn.getOrbitalPeriodYear())











