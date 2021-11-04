"""
最後に卓の種類によって、勝利条件を変更する checkWinner
というメソッドを作成しましょう。
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
    # gameModeを受け取ります。デフォルトはNone
    def __init__(self, gameMode=None):
        self.deck = self.generateDeck(gameMode)

    # デッキを生み出す関数を作成します。
    # staticメソッドを使います。ここではインスタンス無しでも使える関数と考えていただければ問題ありません。
    # 全記号・すべての値を用意し、forで1つずつカードを生成します。
    @staticmethod
    # gameModeを受け取ります。
    def generateDeck(gameMode=None):
        newDeck = []
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # blackJackを追加します。
        blackJack = {"A": 1, "J": 10, "Q": 10, "K": 10}
        suits = ["♣", "♦", "♥", "♠"]

        for suit in suits:
            for i, value in enumerate(values):
                if gameMode == "21":
                    if value in blackJack.keys():
                        newDeck.append(Card(value, suit, (blackJack[value])))
                    else:
                        newDeck.append(Card(value, suit, int(value)))
                else:
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
            # gameModeを渡します。
            "deck": Deck(gameMode)
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

    # 各プレーヤーの手札を受け取って、合計値を計算するscore21Individualメソッドを作成します。
    # ブラックジャックでは値の合計値が21を超えるとNGなのでその場合は0とします。
    @staticmethod
    def score21Individual(cards):
        value = 0
        for card in cards:
            value += card.intValue
        return value if 21 >= value >= 1 else 0

    # ブラックジャックで誰が勝利したか表示する関数を作成します。
    # それぞれのプレイヤーの手札をscore21Individualで計算し、配列に保存します。例: [10,16,15,16,15,15]
    # この場合、勝利するプレイヤーが複数存在することから、cache[10] = 1, cache[15] = 3, cache[16] = 2のように書き換えます。
    # 配列 [10,16,15,16,15,15]の最大値は16で、cache[16] > 1なのでドローになります。
    # もし、0 <= cache[16] <= 1なら、そのプレイヤーの勝利、それ以外の場合は勝者が誰もいないことになります。
    # ではこのロジックを関数にしてみましょう。
    @staticmethod
    def winnerOf21(table):
        points = []
        cache = {}
        for cards in table["players"]:
            point = Dealer.score21Individual(cards)
            # それぞれのpointを配列に保存
            points.append(point)
            if point in cache:
                cache[point] += 1
            else:
                cache[point] = 1
        # 各プレーヤーの得点を確認
        print(points)
        # print(cache)
        winnerIndex = HelperFunctions.maxInArrayIndex(points)

        if cache[points[winnerIndex]] > 1:
            return "It is a draw"
        elif cache[points[winnerIndex]] >= 0:
            return "player " + str(winnerIndex + 1) + " is the winner."
        else:
            return "No winners.."

    # 卓のゲームの種類によって勝利条件を変更するcheckWinnerというメソッドを作成します。
    @staticmethod
    def checkWinner(table):
        if table["gameMode"] == "21":
            return Dealer.winnerOf21(table)
        else:
            return "no game"



# 計算のみを行うHelperFunctionsクラスを定義します。
class HelperFunctions:

    # 数値で構成させる配列を受け取り、最大値のインデックスを返します。
    @staticmethod
    def maxInArrayIndex(intArr):
        maxIndex = 0
        maxValue = intArr[0]
        for i, num in enumerate(intArr):
            if num > maxValue:
                maxValue = num
                maxIndex = i
        return maxIndex

table1 = Dealer.startGame(4, "21")
Dealer.printTableInformation(table1)
print(Dealer.checkWinner(table1))

table2 = Dealer.startGame(1, "poker")
Dealer.printTableInformation(table2)
print(Dealer.checkWinner(table2))




# 最大値は19(= index 2)
# arr1 = [1, 9, 19, 3, 4, 6]
# print(HelperFunctions.maxInArrayIndex(arr1))
#
# # 最大値は5(= index 0)
# arr2 = [5, 2, 1, 3, 5, 5]
# print(HelperFunctions.maxInArrayIndex(arr2))

#
# # PlayerAの手札
# card1 = Card("◆", "A", 1)
# card2 = Card("◆", "J", 11)
#
# card3 = Card("◆", "9", 9)
# card4 = Card("◆", "K", 13)

# print(Dealer.score21Individual([card1, card2]))
# print(Dealer.score21Individual([card3, card4]))

# # 卓の設定 2 player
# table1 = Dealer.startGame(2, "21")
#
# # 卓の情報を表示します
# Dealer.printTableInformation(table1)


# 1人目のplayerの手札をfor文で出力
# for i in range(0, Dealer.initialCards("poker")):
#     print(table1[0][i].getCardString())








