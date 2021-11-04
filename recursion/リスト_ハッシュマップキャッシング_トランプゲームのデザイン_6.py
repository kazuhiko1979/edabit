"""
次はデッキからカードを 1 枚ドローする動作を考えましょう。今 deck は配列なのでそこから pop（末尾を取得）すればカードをドローと同じ挙動を作ることができます。
"""
import random

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
                # print(Card(value, suit, i+1).getCardString())
                newDeck.append(Card(value, suit, i+1))
        return newDeck

    # カードをドロー
    def draw(self):
        return self.deck.pop()


    def printDeck(self):
        print("Displaying cards...")
        for card in self.deck:
            print(card.getCardString())

    # シャッフルする関数はtwo pointerを活用します。
    # for文でカードをランダム入れ替える処理を書きましょう。
    def shuffleDeck(self):
        deckSize = len(self.deck)
        for i in range(0, deckSize):
            j = random.randint(i, deckSize-1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]




deck1 = Deck()
deck1.shuffleDeck()


# ドローしたカードを表示
print(deck1.draw().getCardString())








