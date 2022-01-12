# 連邦税を設定します
federalTaxes = 0.2


# 州の税率を受け取って、所得を受け取り所得税を計算する関数
def taxLambda(stateTax, state):
    def f(income):
        # 連邦税、州税の変数はどちらもスコープ外です。
        # この関数が作成されると、stateTax および federalTaxの状態であれ
        # この関数にバインドされます。作成時の stateTax が0.15 である場合、
        # この関数の stateTax の状態は 0.15 になります。
        taxes = federalTaxes + stateTax

        # 何かが出力された時にログを記録し、 stateの文字列もバインドします。
        print("Computing taxes for state... " + state)
        return int(income - (taxes * income))

    return f

califoriniaF = taxLambda(0.0725, "California")
texasF = taxLambda(0.0625, "Texes")
hawwaiiF = taxLambda(0.04, "Hawaii")

# 税金を計算します。
income = 40000
print("Calculating income using lambdas")
print(califoriniaF(income))
print(texasF(income))
print(hawwaiiF(income))

income2 = 50000
print("-----Calculating more income using lambdas-----")
print(califoriniaF(income2))
print(texasF(income2))
print(hawwaiiF(income2))


import math
# 整数nを受け取り、xを受け取り、x*nを計算する関数を返す
def powerOfNLambda(n):
    def f(x):
        return math.pow(x, n)
    return f

print(powerOfNLambda(3)(2))

# 整数nを受け取り、リストを受け取り、リストをn回複製する関数を返す
def nDuplicateListLambda(n):
    def f(list):
        result = [list for i in range(n)]
        return result
    return f

print(nDuplicateListLambda(2)([1,2,3,4]))







