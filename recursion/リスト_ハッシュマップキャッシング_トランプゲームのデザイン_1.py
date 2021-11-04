"""
ディーラーがデッキのカードをシャッフルし、複数のプレイヤーに対してカードを配り、
ブラックジャックで誰が勝利するかを表示する実装を行っていきます。
オブジェクト、配列が何度も出てくるので今回の例を通じてよく復習しましょう。

では、まずは 1 枚分のカードを表すクラス Card を生成していきます。
"""


class Card:
    # インスタンス生成のためのコンストラクタ
    def __init__(self, value, suit, intValue):
        self.value = value
        self.suit = suit
        self.intValue = intValue

    # オブジェクトの状態を表示する関数
    def getCardString(self):
        return self.suit + self.value + "(" + str(self.intValue) + ")"


card1 = Card("A", "◆", 1)

print(card1.getCardString())



