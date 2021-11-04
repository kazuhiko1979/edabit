"""
今回は卓の情報を表示する printTableInformation というメソッドを作成していきます。
table を受け取り、卓の情報とそれぞれのプレイヤーの手札を表示します。
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

# ディーラークラス（ステートレスオブジェクト）
class Dealer:

    @staticmethod
    def startGame(amountOfPlayer, gameMode):
        # 卓の情報
        table = {
            "players": [],
            "gameMode": gameMode,
            "deck": Deck()
        }

        # デッキをシャッフルします
        table["deck"].shuffleDeck()

        for person in range(0, amountOfPlayer):
            # プレーヤーの手札
            playerCard = []
            # ブラックジャックの手札は2枚
            for i in range(0, Dealer.initialCards(gameMode)):
                playerCard.append(table["deck"].draw())
            table["players"].append(playerCard)
        return table

    # ゲームの内容によって手札を変更します
    @staticmethod
    def initialCards(gameMode):
        if gameMode == "21":
            return 2
        if gameMode == "poker":
            return 5

    # 卓の情報を表示するメソッドを作成します。
    @staticmethod
    def printTableInformation(table):
        print("Amount of players: " + str(len(table["players"])) +
              "... Game mode: " + table["gameMode"] + ". At this table: ")

        for i, player in enumerate(table["players"]):
            print(str(i + 1) + " player's cards")
            for card in player:
                print(card.getCardString())


# 卓の設定 2 player
table1 = Dealer.startGame(2, "poker")

# 卓の情報を表示します
Dealer.printTableInformation(table1)


# 1人目のplayerの手札をfor文で出力
# for i in range(0, Dealer.initialCards("poker")):
#     print(table1[0][i].getCardString())








