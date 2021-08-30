"""
投資の計算


関数の入出力例

入力のデータ型： integer capitalMoney, integer goalMoney, integer interest

出力のデータ型： integer

howLongToReachFundGoal(5421,10421,5) --> 27
howLongToReachFundGoal(5421,30,30) --> 0
howLongToReachFundGoal(600,10400,7) --> 67
howLongToReachFundGoal(32555,5200000,12) --> 58
howLongToReachFundGoal(50,35000,65) --> 14
howLongToReachFundGoal(10,350000,2) --> 80
howLongToReachFundGoal(20000,10050000,30) --> 27
"""

# def howLongToReachFundGoal(capitalMoney, goalMoney, interest):
#
#     year = 0
#     interest_kisuu = 2
#     interest_gusuu = 3
#     land_list = []
#
#     while year < 80:
#
#         if year % 2 == 0:
#             goalMoney = goalMoney * (1 + interest_kisuu / 100)
#             year = year + 1
#             land_list.append(goalMoney)
#         else:
#             goalMoney = goalMoney * (1 + interest_gusuu / 100)
#             year = year + 1
#             land_list.append(goalMoney)
#
#     capital_list = []
#     capital_year = 0
#
#     while capital_year < 80:
#
#         capitalMoney = capitalMoney * (1 + interest / 100)
#         capital_year = capital_year + 1
#         capital_list.append(capitalMoney)
#
#     index_list = []
#
#     for l, c in zip(land_list, capital_list):
#         if l < c:
#             index_list.append(capital_list.index(c))
#
#     # if index_list is None:
#     #     return 80
#     # else:
#     # return index_list[0] + 1
#     if index_list == []:
#         return 80
#     if index_list[0] == 0:
#         return 0
#     else:
#         return index_list[0] + 1

def howLongToReachFundGoal(capitalMoney, goalMoney, interest):
    # helper関数に移ります。
    return howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, 0)


#　引数にyearを追加し、経過年を追加できるようにします
def howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, year):
    # capitalMoney が　goalMoney以上になったら経過年を返します
    if capitalMoney >= goalMoney:
        return year
    if year >= 80:
        return 80

    # 経過年yearが偶数の時はgoalMoneyを2%, 奇数の時3%増加させます
    if year % 2 == 0:
        goalMoney *= 1.02
    else:
        goalMoney *= 1.03

    # capitalMoney に年利を加えます
    capitalMoney *= (1+interest/100)

    # yearに1加えて再帰を行います。
    return howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, year+1)






print(howLongToReachFundGoal(600, 10400, 7))
print(howLongToReachFundGoal(32555,5200000,12))
print(howLongToReachFundGoal(5421,30,30))
print(howLongToReachFundGoal(10,350000,2))






