"""
では、次にデッキ（山札）を作成していきます。デッキを表すクラス Deck を作成し、デッキをコンソールに表示します。
Deck クラスの中にトランプカード全種類を生成するメソッドを作成します。
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


class Deck:
    # コンストラクタ
    def __init__(self):
        self.deck = self.generateDeck()

    # デッキを生み出す関数を作成します。
    # staticメソッドを使います。ここではインスタンス無しでも使える関数と考えていただければ問題ありません。
    # 全記号・すべての値を用意し、forで1つずつカードを生成します。
    @staticmethod
    def generateDeck():
        newDeck = []
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["♣", "♦", "♥", "♠"]

        for suit in suits:
            for i, value in enumerate(values):
                print(Card(value, suit, i+1).getCardString())
                newDeck.append(Card(value, suit, i+1))
        return newDeck

# デッキを生成します
Deck()
# card1 = Card("A", "◆", 1)
# print(card1.getCardString())



