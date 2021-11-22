"""
数式の解析
medium
文字列で表現された数式 expression が与えられるので、その数式を評価し、整数の結果を返す、
expressionParser という関数を作成してください。
ただし、割り算に関しては小数点以下を切り捨てた整数値を返してください。

関数の入出力例

入力のデータ型： string expression

出力のデータ型： integer

expressionParser("2+4*6") --> 26

expressionParser("2*3+4") --> 10

expressionParser("3-3+3") --> 3

expressionParser("2+2+2") --> 6

expressionParser("1-1-1") --> -1

expressionParser("3*3/3*3*3") --> 27

expressionParser("14/3*2") --> 8

expressionParser("12/3*4") --> 16

expressionParser("1+2+3+4+5+6+7+8+9+10") --> 55

expressionParser("1+2*5/3+6/4*2") --> 6

expressionParser("42") --> 42

expressionParser("7*3622*636*2910*183+343/2926/1026") --> 8587122934320

数字と演算子を入れるためのスタックを用意し、
数式をループして現在の文字をそれぞれのスタックに入れていきます。
演算子*,/は+,-よりも優先順位が高いことに注意しましょう。

演算子の優先順位を返す関数、数字のスタックと演算子を受け取って計算する関数を作ります。
計算する関数はID145電卓を参考にしてみましょう。
"""

"""
上級コース / データ構造入門 / スタック(2) の節で、この問題の考え方について詳しく説明していますので確認してください。まずは、数字を入れるためのスタック nums と演算子を入れるためのスタック ops を用意し、数式を歩くようにループして 1 文字ずつ取り出します。


取り出した文字は

(1)数字が来た場合
(2)演算子が来た場合
の 2 つのケースに分けて考えます。


(1) 数字が来た場合の処理
文字列を入れる変数 number を用意し、2 桁以上の数字が来た場合に備えて以下の処理をします。

現在の文字が数値だった場合は number に追加
カウンター変数 i を 1 つ増やして隣の文字をチェック
隣の文字も数値だったら number に追加

while で上記を現在の文字が数値でなくなるまで繰り返し、
出来上がった number の値を数字のスタック nums に push します。

(2) 演算子が来た場合の処置
演算子が来たときには、演算子の優先順位を返す関数 ※1 を呼び出して、
現在の演算子とスタックにすでに入っている演算子の優先順位を比較します。

現在の演算子よりもスタックの演算子の優先順位が低い場合はそのままスタック ops に push。
同じか高い場合には、計算する関数 ※2 を呼び出して計算します。
スタックに入っている演算子を削除して、現在の演算子をスタックに入れます。

20 * 3 + 6 の例を見てみますと、最初の文字は 2 ですが、
数式では 20 なので 2 桁以上の場合のを処理をしスタックに 20 が入ります。
nums[20]
ops[]

次にくる演算子 '*' は、まだ演算子のスタックに何も入っていないのでそのままスタックに入ります。
nums[20]
ops['*']

その次の 3 は数字なので数字のスタックに入ります。
nums[20,3]
ops['*']

次の '+' が来たとき、'*' の優先順位は '+' のそれより高いので、先に計算をします。
nums に入っている 20 と 3 を取り出して、かけた値 60 を数字のスタックに入れます。
'*' は削除して '+' をスタックに入れます。
nums[60]
ops['+']

最後の文字 6 をスタックに入れます。
nums[60,6]
ops['+']

文字列の最後まで到達したので、スタックに残っている要素を計算していきます。
ops が空になるまで計算する関数を呼び出し、結果を数字のスタックに入れます。
ops が空になった時、nums の先頭に答えが入っています。

※1 演算子の優先順位を返す関数
'','/','+','-' の優先順位を数値で返します。
'','/' は 2、'+','-'は 1 を返すように条件分岐か、ハッシュマップを作ります。

※2 計算をする関数
スタックと演算子を受け取って、スタックの要素 2 つを取り出し計算する関数を作ります。
この関数は void（戻り値がない）で、計算した答えを再度スタックに入れて次の計算に使います。
"""

from collections import deque

def expressionParser(expression):

    nums = deque([]) # 数字を入れるためのスタック
    ops = deque([]) # 演算子を入れるためのスタック

    i = 0
    while i < len(expression):
        if not expression[i].isdigit():
            # 演算子が来た時の処理
            currOP = expression[i]
            # 現在の演算子とスタックに入っている演算子の優先順位を比較します。
            # スタックに入っている演算子の方が優先順位が高い時に計算します。
            while len(ops) > 0 and getPriority(currOP) <= getPriority(ops[-1]):
                process(nums, ops.pop())
            ops.append(currOP)

        # 数字が来た時の処理　ここでは文字列として扱います。
        else:
            number = ''
            # 2桁以上の数字に対応するため、演算子がくるまで文字を結合していきます。
            while i < len(expression) and expression[i].isdigit():
                number += expression[i]
                i += 1

            i -= 1 # 最後に増やしたiを1つ戻しておきます。
            nums.append(int(number))
        i += 1

    # 演算子のスタックが空になるまでprocessを呼び出して計算を続けます。
    while len(ops) > 0:
        process(nums, ops.pop())

    # 数字のスタックの先頭に答えが入っています。
    return nums[0]


# スタックから数字を取り出し、受け取った演算子で計算する関数
def process(stack, op):
    # 数字のスタックから文字列を取り出し数字にします。
    right = int(stack.pop())
    left = int(stack.pop())

    value = 0

    if op == "+":
        value = left + right
    if op == "-":
        value = left - right
    if op == "*":
        value = left * right
    if op == "/" and right == 0:
        value = left
    elif op == "/":
        value = left // right

    # 計算した結果は、次の演算子での計算のため、再度スタックに入れます。
    stack.append(value)

# 演算子の優先順位を返す関数
def getPriority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2

# print(expressionParser("2+4*6"))
# print(expressionParser("2*3+4"))



