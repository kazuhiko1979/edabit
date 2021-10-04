"""
ィットネスアプリケーションを例に見てみましょう。Person オブジェクトを作成します。設計図は以下のように定義されます。

// ヒトは以下のような状態を持っています。
String firstName: // 苗字
String lastName: // 名前
double heightM: // 身長（メートル）
double weigthKg: // 体重（キログラム）
int birthYear: // 生まれた年

String person.getFullName(): // フルネームを返します。
String person.getAge(): // 年齢を返します。
double person.getBmi(): // BMIを返します。
double person.eat(int calories): // 体重を更新し、新しい体重を返します。

double person.caloriesBurnedPerMinuteExercise(string exercise):
// 運動を文字列として受け取り、1分間に消費されたカロリー数を返します

double person.exercise(string exercise, int minutes):
// 燃焼されたカロリー数を計算し、体重を更新して新しい体重を返します。

double person.hoursToLose1KgByExercise(string exercise):
// 運動を文字列として受け取り、1㎏痩せるのに何時間かかるかを返します。

"""
import datetime

class Person:

    def __init__(self, firstName, lastName, heightM, weightKg, birthYear):
        self.firstName = firstName
        self.lastName = lastName
        self.heightM = heightM
        self.weightKg = weightKg
        self.birthYear = birthYear

    def getStateString(self):

        return "First Name: " + self.firstName + ", Last Name: " + self.lastName + \
    ", heightM: " + str(self.heightM) + ", weightKg:" + str(self.weightKg) + \
    ", birthYear:" + str(self.birthYear)


    def getFullName(self):

        return self.firstName + " " + self.lastName

    def getAge(self):

        """
        datetimeライブラリを使って、現在の年を取得します。
        datetime.datetime.now()は今を表すオブジェクトを返します。このオブジェクトの中には
        year, month, hour, minuteなどの変数があります。
        :return:
        """
        currentYear = datetime.datetime.now().year
        return currentYear - self.birthYear

    def getBmi(self):
        # BMIの公式は、体重(kg) / 高さ(m)の2乗です。
        return self.weightKg / (self.heightM ** 2)

    def eat(self, calories):
        # ユーザーの体重を消費されたカロリーに基づいて更新します。現在の体重を返します。
        # 7700カロリーにつき、1キロ増加します。
        self.weightKg += calories / 7700
        return self.weightKg


    def caloriesBurnedPerMinuteExercise(self, exercise):
        # 運動を文字列として受け取り、1分間に消費されたカロリー数を返します
        # 燃焼カロリーはMET（Metabnolic Equivalent of Task)を使って計算することができます。

        met = 1
        if exercise == "running":
            met = 8
        elif exercise == "walking":
            met = 3
        elif exercise == "tennis":
            met = 5
        elif exercise == "rope jump":
            met = 9
        # 燃焼カロリーは met * 3.5 * self.weightKg / 200 によって計算することができます。

        return met * 3.5 * self.weightKg / 200

    def exercise(self, exercise, minutes):
    # 燃焼されたカロリー数を計算し、体重を更新して新しい体重を返します。

    #     return self.weightKg - (self.caloriesBurnedPerMinuteExercise(exercise) * minutes / 7700)

    # 関数の分解
        caloriesBurned = self.caloriesBurnedPerMinuteExercise(exercise) * minutes
        self.weightKg -= caloriesBurned / 7700
        return self.weightKg

    def hoursToLose1KgByExercise(self, exercise):
    # 運動を文字列として受け取り、1㎏痩せるのに何時間かかるかを返します。
    # 1kg > 7700kcl
        return 7700 / (self.caloriesBurnedPerMinuteExercise(exercise) * 60)



# mike = Person("Michael", "Johnson", 1.72, 85.5, 1988)
carly = Person("Carly", "Angelo", 1.72, 85.5, 1996)

# print(mike.getStateString())
print(carly.getStateString())
#
# print(carly.getFullName())
# print(carly.getAge())
# print(carly.getBmi())
#
# print(mike.getFullName())
# print(mike.getAge())
# print(mike.getBmi())
#
# # calryの状態を出力します
# print(carly.getStateString())
# carly.eat(2400)
# print(carly.getStateString())

print("Carly burns: " + str(carly.caloriesBurnedPerMinuteExercise("running")) + \
      " calories per minute running")

print("It taks carly: " + str(carly.hoursToLose1KgByExercise("running")) + \
      " hours running to burn 1 kg")

carly.exercise("running", 600)
print("Calry went to running for 10 hours")
print(carly.getStateString())







