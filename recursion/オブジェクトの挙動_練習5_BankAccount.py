"""
あなたは銀行をシュミレーションするビデオゲームに機能を追加しています。
この銀行はプレイヤーのお金を BankAccount で管理し、いくつかの機能を提供します。
この銀行では、整数で表される、☦ という通貨によってお金が管理されます。
☦1000 によってポテトチップス 1 袋購入できるとします。
"""

"""
状態
String backName // 銀行口座を管理する銀行名
String ownerName // 銀行口座の所有者の名前
int savings // 銀行口座の中に現在ある合計貯蓄額
double interestPerDay // 銀行が所有者に課す1日の利息の合計。デフォルトは1.0001%で、それ以下になることはありません。
"""

"""
挙動
String showInfo() // ユーザーの情報を返します。口座番号は1から10(8)までの整数の中からランダムに選択するように、
他にgetRandomIntegerという関数を作成してください。

/*
例
bank: chase
owner name: Claire Simmons
bank account number: 52574092
*/

int depositMoney(int depositAmount) // depositAmountによって貯蓄額を増やし、
その金額をint型で返します。もし預金前の貯蓄額が$20,000以下の場合は、$100の手数料がかかります。

int withdrawMoney(int withdrawAmount) // withdrawAmountによって貯蓄額を減らし、
withdrawAmountを整数として返します。最大で貯蓄額の20%を引き出すことができます。

double pastime(int day) // 毎日interestPerDayによって貯蓄額を増加し、その金額をdouble型で返します。
"""
import math
import random


class BankAccount:

    maxWidthdrawRate = 0.2

    def __init__(self, bankName, ownerName, savings, interestPerDay):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings
        self.interestPerDay = interestPerDay

    def showInfo(self):

        return "bank: " + self.bankName + "\nowner name: " + self.bankName + \
                "\nbank account number: " + str(self.HelperFunction.getRandomInteger(1, math.pow(10, 8)))

    def withdrawMoney(self, withdrawAmount):
        moneyYouCanTake = self.maxWidthdrawRate * self.savings if withdrawAmount > self.maxWidthdrawRate * self.savings else withdrawAmount
        self.savings -= moneyYouCanTake
        return int(moneyYouCanTake)

    def depositMoney(self, depositAmount):

        self.savings += depositAmount - 100 if self.savings <= 20000 else depositAmount
        return int(self.savings)

    def pastime(self, day):
        return self.savings * (1 + self.interestPerDay) ** day

    # 計算を行うクラス
    class HelperFunction:
        # min-max間のランダムな整数を返します。
        @staticmethod
        def getRandomInteger(min, max):
            return math.floor(random.random() * (max - min)) + min

user1 = BankAccount("Chase", "Claire Simmons", 30000, 0.010001)

print(user1.showInfo())
print(user1.withdrawMoney(1000))
print(user1.depositMoney(10000))
print(user1.pastime(200))

print("\n")

user2 = BankAccount("Bank of America", "Remy Clay", 10000, 0.010001)

print(user2.showInfo())
print(user2.withdrawMoney(5000))
print(user2.depositMoney(12000))
print(user2.pastime(500))








