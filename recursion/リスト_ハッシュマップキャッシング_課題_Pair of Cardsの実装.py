"""
ペアの強さ
A < AA < AAA < AAAA < AAAAA

カードの強さ
2 < 3 < 4 < 5 < 6 … J < Q < K < A

2 人のプレイヤーがカードをドローし、以下のルールによって、勝敗を決定します。
- 同じランク（※カードの強さ）のカードの枚数が多いプレイヤーが勝利する（2が3枚 > 10が2枚）
- 上記枚数が同じ場合は、そのカードのランクによって勝敗が決まる（2が2枚 < 10が2枚）
- 上記も同じ場合は、次に枚数の多いカードを同様に比べ、勝敗が決まるまですべてのカードを比べる。
- 最終的に勝敗が決まらない場合はdrawとする
※ カードの強さ : 2 < 3 < 4 < 5 < 6 … J < Q < K < A

Case1: プレイヤー1 が ["♣4","♥8","♥8","♠8","♣J"] で、プレイヤー2 が ["♣4","♥J","♥J","♠Q","♣3"] の場合、
プレイヤー1 は 8 を 3 枚持ち、プレイヤー2 は J を 2 枚持っているので、プレイヤー1 が勝利します。

Case2: プレイヤー1 が ["♣4","♥8","♥8","♠4","♣J"] で、プレイヤー2 が ["♣4","♥J","♥J","♠Q","♣3"] の場合、
プレイヤー1 は 4 を 2 枚、8 を 2 枚持ち、プレイヤー2 は J を 2 枚持つので、両者のランクの数は同じです。一方、両者のカードを比較してみると、
プレイヤー2 のカード（J）の方がプレイヤー1（8）よりも強いので、プレイヤー2 の勝利となります。

Case3: プレイヤー1 が ["♣4","♥7","♥7","♠Q","♣J"] で、プレイヤー2 が ["♥7","♥7","♣K","♠Q","♦2"] の場合、プレイヤー1 は 7 を 2 枚持ち、
プレイヤー2 も 7 を 2 枚持つので、両者のランクの数もカードの強さも同じです。次に 1 枚のカードを見ると、
プレイヤー2 のカード K の方がプレイヤー1 Q よりも強いので、プレイヤー2 の勝利となります。

カード、デッキ、ディーラーをそれぞれ 1 から自分の力で作成し、「Pair of Cards」を設計しましょう。
"""
import math
import random

# カードクラス
class Card:
    def __init__(self, suit, value, intValue):
        self.suit = suit
        self.value = value
        self.intValue = intValue

    # カードを表示するメソッド　例　♡K（13）
    def getCardString(self):
        return self.suit + self.value + "(" + str(self.intValue) + ")"

# デッキクラス
class Deck:
    def __init__(self, gameMode = None):
        self.deck = self.generateDeck()

    # デッキ(山札）を作成します
    @staticmethod
    def generateDeck():
        suit = ["♣", "♦", "♥", "♠"]
        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        newDeck = []
        intValue = 1
        for i in suit:
            for j in value:
                newDeck.append(Card(i, j, intValue))
                intValue +=1
            intValue=1
        return newDeck

    # カードを表示するメソッド
    def printDeck(self):
        for i in range(len(self.deck)):
            print(self.deck[i].getCardString())

    # カードをシャッフルするメソッド
    def shuffleDeck(self):
        deckSize = len(self.deck)
        for i in range(0, deckSize):
            j = random.randint(i, deckSize-1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

            # temp = self.deck[i]
            # self.deck[i] = self.deck[j]
            # self.deck[j] = temp

    # カードを1枚引くメソッド
    def draw(self):
        return self.deck.pop()

# ディーラークラス
class Dealer:

    # ディーラーはカードをシャッフルしプレイヤーにカードを配ります。
    @staticmethod
    def startGame(amountOfPlayers, gameMode):
        table = {
            "players": [],
            "gameMode": gameMode,
            "deck": Deck(gameMode)
        }
        table["deck"].shuffleDeck()

        for person in range(0, amountOfPlayers):
            playerCard = []
            for i in range(0, Dealer.initialCards(gameMode)):
                playerCard.append(table["deck"].draw())
            table["players"].append(playerCard)

        return table

    # ゲームモードによって配るカードの枚数を返すメソッド
    @staticmethod
    def initialCards(gameMode):
        if gameMode == "porker":
            return 5
        if gameMode == "21":
            return 2
        if gameMode == "Pair of Cards":
            return 5

    # テーブルの状態を表示するメソッド
    @staticmethod
    def printTableInfo(table):
        print("Amount of players: " + str(len(table["players"])) + "\nGamemode: " + table["gameMode"])

        for i in range(len(table["players"])):
            print("\nPlayer " + str(i + 1))
            for j in range(len(table["players"][i])):
                print(table["players"][i][j].getCardString())

    # ゲームの勝敗を決める関数
    @staticmethod
    def winnerPairOfCards(table):
        # 同じ数字をたくさん持っているプレイヤーの勝ち
        # 枚数が同じなら数字が大きいプレイヤーの勝ち

        # カードの強さ ：2 < 3 < 4 < 5 < 6 … J < Q < K < A
        cardPower = [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

        # 数字だけの配列を作ります。
        numbers1 = Helperfunction.generateNumberArr(table["players"][0])
        numbers2 = Helperfunction.generateNumberArr(table["players"][1])

        print(numbers1)
        print(numbers2)

        # プレイヤーのカードをハッシュマップにします。
        hashmap1 = Helperfunction.createHashmap(cardPower, numbers1)
        hashmap2 = Helperfunction.createHashmap(cardPower, numbers2)

        # デフォルトで引き分けを返します。
        winner = "draw"

        # 同じランクのカードの枚数を記録します。
        pairOfCards = 0

        for i in range(len(cardPower)):
            # それぞれのhashmapをcardPowerの強い順に比較していきます。
            # 0または同じ枚数の時は次のランクへ
            # プライヤー1が持つ同じランクのカードが多いとき
            if hashmap1[cardPower[i]] > hashmap2[cardPower[i]]:
                # 記録しているカードの枚数よりプレイヤー1が持つカードの枚数が多かったら、
                if pairOfCards < hashmap1[cardPower[i]]:
                    # pairOfCardsとwinnerをプレイヤー1に書き換えます。
                    pairOfCards = hashmap1[cardPower[i]]
                    winner = "player 1."
            elif hashmap1[cardPower[i]] < hashmap2[cardPower[i]]:
                if pairOfCards < hashmap2[cardPower[i]]:
                    pairOfCards = hashmap2[cardPower[i]]
                    winner = "player 2."
        print("The winner of self game is ")
        return winner


class Helperfunction:

    # 数字だけの配列を作ります。
    @staticmethod
    def generateNumberArr(playerhand):
        intArr = []
        for i in range(len(playerhand)):
            intArr.append(playerhand[i].intValue)
        # print(intArr)
        return intArr

    # Hashmapを作成
    @staticmethod
    def createHashmap(cardPower, numberArr):

        hashmap = {}
        for i in range(len(cardPower)):
            hashmap[cardPower[i]] = 0

        for i in range(len(numberArr)):
            hashmap[numberArr[i]] += 1
        print(hashmap)
        return hashmap


table = Dealer.startGame(2, "Pair of Cards")
Dealer.printTableInfo(table)
print("-" * 50)
print(Dealer.winnerPairOfCards(table))












