"""
最後に卓の種類によって、勝利条件を変更する checkWinner
というメソッドを作成しましょう。
"""
"""
Best solution
1. カードから "♥" や "♣" など 4 種類の図柄を取り除き、数字と A, J, Q, K だけの配列を作る
2. 13 種類のカードのうち、どのカードを持っているのかを記録するハッシュマップを作る
3. 勝利条件に合わせて条件分岐を作る。
"""

"""
1. 数字と A, J, Q, K だけの配列を返す generateNumberArr() 関数を作ります。

カードは "♣4" "♣K" のように、絵柄と、数字（アルファベット）の組み合わせになっていますので、
勝負の判定に影響しない絵柄を取り除いて、数字または A, J, Q, Kのアルファベットのみの配列にします。
substring メソッドを使って 2 番目の文字（インデックスでは 1）以降の文字列を切り出します。
※PHP の substr メソッドはバイト数を使うため、インデックスは 3 になります（♣ は 3 バイト）。
プレイヤーが持っているカードの枚数だけ for 文で繰り返して、新しく作成した配列に切り出した文字列をプッシュします。
"""

# 受け取ったカードの配列から"♡"や"♠"など4種類の図柄を取り除き、ランクだけの配列を作ります。
def generateNumberArr(playerHand):
    rankArr = []

    for i in range(len(playerHand)):
        # substringメソッドを使って、先頭の絵文字以外を切り出します。
        rankArr.append(playerHand[i][1:])

    # ランクだけになった配列を返します。
    return rankArr

# print(generateNumberArr(["♣4","♥7","♥7","♠Q","♣J"]))
# print(generateNumberArr(["♣4","♥7","♥7","♠Q","♣J"]))
# print(generateNumberArr(["♣A","♥2","♥3","♠4","♣5"]))

"""
2. 数字とアルファベットだけになった配列をハッシュマップにする createHashmap() 関数を作ります。
カードは 13 種類しかないので、13 個の要素を持つハッシュマップを作成します。
キーは数字またはアルファベット、バリューは 0 で埋めます。
{"A":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "J":0, "Q":0, "K":0}。1 で作った配列を for 文で繰り返して、どのカードを何枚持っているのかハッシュマップに記録します。例えば、["♣4","♥7","♥7","♠Q","♣J"] のカードを持っていた場合、{"A":0, "2":0, "3":0, "4":1, "5":0, "6":0, "7":2, "8":0, "9":0, "10":0, "J":1, "Q":1, "K":0} 
というハッシュマップが作成されます。

注意をしなければいけないのは、カードの強さは 2 < 3 < 4 < 5 < 6 … J < Q < K < A になっていることです。
そこでカードを強い順で並べ替えた配列を作ります。
この配列は変更しないので定数に入れましょう。
const cardPower = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
"""

# ハッシュマップを作る関数
def createHashmap(cardPower, numberArr):
    hashmap = {}
    # cardPower = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

    # A-Kまで13枚のカードのうち、どのカードをもっている記録するため、まずは0で埋めたハッシュマップを作ります。
    for i in range(len(cardPower)):
        hashmap[cardPower[i]] = 0

    # ランクだけになったカードの配列から、持っているカードをハッシュマップに記録します。
    for i in range(len(numberArr)):
        hashmap[numberArr[i]] += 1
    return hashmap

# print(createHashmap(generateNumberArr(["♣4","♥7","♥7","♠Q","♣J"])))

"""
3. 勝利条件に合わせて条件分岐をする

プレイヤー1、プレイヤー2 それぞれのハッシュマップを作成したら、勝利条件に合わせて分岐を作り、判定をします。このゲームの勝利条件は

- 同じランク（※カードの強さ）のカードの枚数が多いプレイヤーが勝利する
- 上記枚数が同じ場合は、そのカードのランクによって勝敗が決まる
- 上記も同じ場合は、次に枚数の多いカードを同様に比べ、勝敗が決まるまで全てのカードを比べる
- 最終的に勝敗が決まらない場合は draw とする
"""


"""
まず最初に、プレイヤー1 もプレイヤー2 も、同じランクのカードを同じ枚数だけ持っている場合を考えます。

プレイヤー1 ["♥7","♥7","♠K","♣Q","♣2"]
プレイヤー2 ["♥7","♥7","♣K","♠Q","♦2"]
というカードを持っていた場合、それぞれのプレイヤーのハッシュマップはこのようになります。

プレイヤー1 
{"A":0, "2":1, "3":0, "4":0, "5":0, "6":0, "7":2, "8":0, "9":0, "10":0, "J":0, "Q":1, "K":1}
プレイヤー2 
{"A":0, "2":1, "3":0, "4":0, "5":0, "6":0, "7":2, "8":0, "9":0, "10":0, "J":0, "Q":1, "K":1}
この場合は、引き分けなので、デフォルトで winner = "draw" としておきます。


次に、同じランクのカードの枚数が多いプレイヤーが勝利する条件について考えてみます。

プレイヤー1 
["♣4","♥8","♥8","♠8","♣J"]
プレイヤー2
["♣4","♥J","♥J","♠Q","♣3"]

プレイヤー1
{"A":0, "2":0, "3":0, "4":1, "5":0, "6":0, "7":0, "8":3, "9":0, "10":0, "J":1, "Q":0, "K":0}
プレイヤー2
{"A":0, "2":0, "3":1, "4":1, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "J":2, "Q":1, "K":0}

先ほど作った cardPower の配列を for 文でループして比較していきます。cardPower = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]。

i = 0
一番強いカードである "A" を比較します。プレイヤー1 もプレイヤー2 も "A" は持っていません。
ハッシュマップどちらもは 0 なので次のランクへ移ります。

i = 1
その次のランクは "K"。これも持っていないためどちらも0。次のランクへ移ります。

i = 2　
プレイヤー2 は "Q" のカードを 1 枚持っていますが、プレイヤー1 は持っていません。
暫定の winner = "draw" を書き換えて winner = "player2" とします。
また、この時のカードの枚数を pairOfCard = 1 として記録します。

i = 3
その次は "J" で、プレイヤー1 が 1 枚、プレイヤー2 が 2 枚持っています。
暫定の勝利者は "player2" のままで、カードの枚数を 2 に書き換えます。
・
・
・
i = 6
この時プレイヤー1 は "8" のカードを 3 枚持っています。
暫定の勝利者をプレイヤー1、カードの枚数を 3 に書き換えます。

i = 10
"4" のカードはどちらも 1 枚ずつ持っています。
どちらも同じ枚数の場合は何もせず次へ移ります。

i = 11 
"3" のカードはプレイヤー2 は 1 枚、プレイヤー1 は持っていません。
プレイヤー2 の方が枚数は多いのですが、記録している "8" の時のカードの枚数は 3 なので、暫定の勝利者を書き換えずに次へいきます。
ループが i = 12 まで来たら、"8" を 3 枚持っていたプレイヤー1 を勝利者として返します。


次はカードの枚数がどちらも同じだった場合について考えます。

プレイヤー1
["♣4","♥8","♥8","♠4","♣J"]
プレイヤー2
["♣4","♥J","♥J","♠Q","♣3"]

プレイヤー1 
{"A":0, "2":0, "3":0, "4":2, "5":0, "6":0, "7":0, "8":2, "9":0, "10":0, "J":1, "Q":0, "K":0}
プレイヤー2 
{"A":0, "2":0, "3":1, "4":1, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "J":2, "Q":1, "K":0}
このパターンはプレイヤー1 が "4" と "8" を 2 枚ずつ、プレイヤー2 が "J" を 2 枚持っていてどちらも同じ枚数です。const cardPower = 
["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]。cardPower を for 文で比較しながら進むと、i=3 のとき、プレイヤー2 が "J" を 2 枚持っています。暫定の勝利者をプレイヤー2 とし、カードの枚数を 2 と記録します。その後ループを繰り返しても、カードの枚数 2 を超えることがないので、プレイヤー2 を勝利者として返します。


では次に、同じランクのカードを同じ枚数だけ持っていた時を考えてみます。

プレイヤー1 
["♣4","♥7","♥7","♠Q","♣J"]
プレイヤー2
["♥7","♥7","♣K","♠Q","♦2"]

プレイヤー1
{"A":0, "2":0, "3":0, "4":1, "5":0, "6":0, "7":2, "8":0, "9":0, "10":0, "J":1, "Q":1, "K":0}
プレイヤー2 
{"A":0, "2":1, "3":0, "4":0, "5":0, "6":0, "7":2, "8":0, "9":0, "10":0, "J":0, "Q":1, "K":1}
このパターンはプレイヤー1 もプレイヤー2 も 7 を 2 枚ずつ、同じランクを同じ枚数だけ持っています。const cardPower = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]。cardPower を for 文でループさせてみましょう。

i = 0
"A" はどちらも持っていないので次へ。

i = 1
"K" のカードをプレイヤー1 が 1 枚持っています。暫定の勝利者をプレイヤー1 としてカードの枚数 1 を記録します。

i = 2
"Q" のカードをプレイヤー2 が 1 枚持っていますが、記録しているカードの枚数 1 と同じなので何もせず次へ移ります。
・
・
・
i = 7
"7" のカードを 2 枚持っていますが、どちらも同じ枚数なので何もせず次へ移ります。
その後も、"K" の 1 枚を書き換えることなく最後までループして、プレイヤー1 を勝利者として返します。

"""

"""
以上の内容をまとめてみます。

・カードの枚数がどちらも0、または同じ枚数の時は暫定の勝利者を書き換えることなく次のループへ移る。
・どちらかが多い場合、記録していたカードの枚数と比較してそれより多かったら、暫定の勝利者とカードの枚数を書き換える。
"""

# カードの強さ : 2 < 3 < 4 < 5 < 6 … J < Q < K < A
def winnerPairOfCards(player1, player2):
    # 強いカードから比較できるように、強さの順にランクを並び替えた配列を作ります。
    cardPower =  ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

    # player1, player2それぞれのカードをランクだけの配列にします。
    numbers1 = generateNumberArr(player1)
    numbers2 = generateNumberArr(player2)

    # print(numbers1)
    # print(numbers2)

    # ハッシュマップを関数を呼び出し
    hashmap1 = createHashmap(cardPower, numbers1)
    hashmap2 = createHashmap(cardPower, numbers2)

    # print(hashmap1)
    # print(hashmap2)

    # デフォルトでは"draw"を返す
    winner = "draw"
    # 同じランクのカードが多いものを探します。
    pairOfCards = 0

    for i in range(len(cardPower)):
        # 強いカードから順にハッシュマップを比較していきます。
        # それぞれのハッシュマップの値がともに、0、または同じ値の時には、次のランクに移ります。
        # プレイヤー１のカードが多かった時
        if hashmap1[cardPower[i]] > hashmap2[cardPower[i]]:
            # 今の最大値であるpairOfCardsよりもプレイヤー1のカード枚数が多かったら書き換えます。
            if pairOfCards < hashmap1[cardPower[i]]:
                pairOfCards = hashmap1[cardPower[i]]
                winner = "player1"
        # プレイヤー2のカードが多かった時
        elif hashmap1[cardPower[i]] < hashmap2[cardPower[i]]:
            if pairOfCards < hashmap2[cardPower[i]]:
                winner = "player2"

    return winner


#--------------------------

# import collections
#
# def winnerPairOfCards(player1, player2):
#
#     values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#
#     scoreList = {value: str(key+1) for key, value in enumerate(values)}
#
#     scorePlayer_1 = []
#     scorePlayer_2 = []
#
#     # 値から、キーを取得(再帰）
#     def get_keys_from_value(dic, key):
#         value = [v for k, v in dic.items() if k == key]
#         return int(value[0])
#
#     # カードの数値をポイント変換し、リストに格納
#     for i in player1:
#         scorePlayer_1.append(get_keys_from_value(scoreList, i[1:]))
#
#     for x in player2:
#         scorePlayer_2.append(get_keys_from_value(scoreList, x[1:]))
#
#     scorePlayer_1 = sorted(scorePlayer_1, reverse=True)
#     scorePlayer_2 = sorted(scorePlayer_2, reverse=True)
#
#     pairsPlayer_1 = dict(collections.Counter(scorePlayer_1))
#     pairsPlayer_2 = dict(collections.Counter(scorePlayer_2))
#
#     # 再帰判定
#     def recursive_judge(re_player1, re_player2):
#
#         maxScorePlayer_1 = max(re_player1.values())
#         maxScorePlayer_2 = max(re_player2.values())
#
#         maxPairsScorePlayer_1 = [key for key, val in re_player1.items() if val == maxScorePlayer_1][0]
#         maxPairsScorePlayer_2 = [key for key, val in re_player2.items() if val == maxScorePlayer_2][0]
#
#         maxPairsCount_player_1 = re_player1[maxPairsScorePlayer_1]
#         maxPairsCount_player_2 = re_player2[maxPairsScorePlayer_2]
#
#         if maxPairsCount_player_1 > maxPairsCount_player_2:
#             return "player1"
#         elif maxPairsCount_player_2 > maxPairsCount_player_1:
#             return "player2"
#         # 上記枚数が同じ場合は、そのカードのランクによって勝敗が決まる（2 が 2 枚 < 10 が 2 枚）
#         elif maxPairsScorePlayer_1 > maxPairsScorePlayer_2:
#             return "player1"
#         elif maxPairsScorePlayer_2 > maxPairsScorePlayer_1:
#             return "player2"
#         else:
#             pairsPlayer_1.pop(maxPairsScorePlayer_1)
#             pairsPlayer_2.pop(maxPairsScorePlayer_2)
#
#             if pairsPlayer_1 == {}:
#                 return "draw"
#             else:
#                 return recursive_judge(pairsPlayer_1, pairsPlayer_2)
#
#     return recursive_judge(pairsPlayer_1, pairsPlayer_2)


print(winnerPairOfCards(["♣4","♥7","♥7","♠Q","♣J"],["♥10","♥6","♣K","♠Q","♦2"]))
print(winnerPairOfCards(["♣4","♥7","♥7","♠Q","♣J"],["♥7","♥7","♣K","♠Q","♦2"]))
print(winnerPairOfCards(["♣A","♥2","♥3","♠4","♣5"],["♥A","♥2","♣3","♠4","♦5"]))
print(winnerPairOfCards(["♣A","♥A","♥A","♠4","♣5"],["♥A","♥A","♣A","♠4","♦5"]))
print(winnerPairOfCards(["♣9","♥8","♥7","♠4","♣5"],["♥10","♥8","♣7","♠4","♦5"]))
print(winnerPairOfCards(["♣A","♥A","♥2","♠3","♣4"],["♥6","♥6","♣Q","♠Q","♦8"]))
print(winnerPairOfCards(["♣A","♥A","♥A","♠3","♣4"],["♥6","♥6","♣Q","♠Q","♦Q"]))
print(winnerPairOfCards(["♣K","♥K","♥K","♠A","♣A"],["♥6","♥6","♣Q","♠Q","♦Q"]))
print(winnerPairOfCards(["♣6","♠3","♠J","♦2","♥3"],["♠8","♥2","♦8","♥9","♦J"]))
print(winnerPairOfCards(["♥3","♠9","♦3","♣Q","♦A"],["♥4","♥3","♠10","♦3","♥4"]))
print(winnerPairOfCards(["♥3","♠9","♦3","♣Q","♦3"],["♥4","♥A","♠10","♦A","♥4"]))
print(winnerPairOfCards(["♣K","♥8","♥K","♠K","♣A"],["♥K","♥4","♣K","♠4","♦K"]))
print(winnerPairOfCards(["♥9","♠8","♦7","♣6","♦5"],["♥9","♥8","♠7","♦6","♥4"]))
print(winnerPairOfCards(["♥3","♠4","♦5","♣6","♦7"],["♥2","♥3","♠5","♦6","♥7"]))
print(winnerPairOfCards(["♥K","♠4","♦K","♣6","♦6"],["♥6","♥K","♠K","♦6","♥7"]))
print(winnerPairOfCards(["♥2","♠2","♦2","♣2","♦6"],["♥2","♥2","♠2","♦2","♥7"]))
print(winnerPairOfCards(["♥2","♠2","♦2","♣2","♦6","♠3","♦3","♣4","♦6"],["♥2","♥2","♠2","♦3","♥7","♠2","♦3","♣6","♦6"]))
print(winnerPairOfCards(["♥2","♠2","♦2","♣2","♦6","♠3","♦3","♣4","♦3"],["♥2","♥2","♠2","♦3","♥7","♠2","♦3","♣6","♦6"]))
print(winnerPairOfCards(["♥2","♠2","♦6"],["♥2","♥2","♥3"]))
print(winnerPairOfCards(["♥2","♠A","♦6"],["♥2","♥2","♥3"]))













# import random
#
# class Card:
#     # インスタンス生成のためのコンストラクタ
#     def __init__(self, value, suit, intValue):
#         self.value = value
#         self.suit = suit
#         self.intValue = intValue
#
#     # オブジェクトの状態を表示する関数
#     def getCardString(self):
#         return self.suit + self.value + "(" + str(self.intValue) + ")"
#
#
# class Deck:
#     # gameModeを受け取ります。デフォルトはNone
#     def __init__(self, gameMode=None):
#         self.deck = self.generateDeck(gameMode)
#
#     # デッキを生み出す関数を作成します。
#     # staticメソッドを使います。ここではインスタンス無しでも使える関数と考えていただければ問題ありません。
#     # 全記号・すべての値を用意し、forで1つずつカードを生成します。
#     @staticmethod
#     # gameModeを受け取ります。
#     def generateDeck(gameMode=None):
#         newDeck = []
#         values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#         # blackJackを追加します。
#         blackJack = {"A": 1, "J": 10, "Q": 10, "K": 10}
#         suits = ["♣", "♦", "♥", "♠"]
#
#         for suit in suits:
#             for i, value in enumerate(values):
#                 if gameMode == "21":
#                     if value in blackJack.keys():
#                         newDeck.append(Card(value, suit, (blackJack[value])))
#                     else:
#                         newDeck.append(Card(value, suit, int(value)))
#                 else:
#                     newDeck.append(Card(value, suit, i+1))
#         return newDeck
#
#     # カードをドロー
#     def draw(self):
#         return self.deck.pop()
#
#
#     def printDeck(self):
#         print("Displaying cards...")
#         for card in self.deck:
#             print(card.getCardString())
#
#     # シャッフルする関数はtwo pointerを活用します。
#     # for文でカードをランダム入れ替える処理を書きましょう。
#     def shuffleDeck(self):
#         deckSize = len(self.deck)
#         for i in range(0, deckSize):
#             j = random.randint(i, deckSize-1)
#             self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
#
# # ディーラークラス（ステートレスオブジェクト）
# class Dealer:
#
#     @staticmethod
#     def startGame(amountOfPlayer, gameMode):
#         # 卓の情報
#         table = {
#             "players": [],
#             "gameMode": gameMode,
#             # gameModeを渡します。
#             "deck": Deck(gameMode)
#         }
#
#         # デッキをシャッフルします
#         table["deck"].shuffleDeck()
#
#         for person in range(0, amountOfPlayer):
#             # プレーヤーの手札
#             playerCard = []
#             # ブラックジャックの手札は2枚
#             for i in range(0, Dealer.initialCards(gameMode)):
#                 playerCard.append(table["deck"].draw())
#             table["players"].append(playerCard)
#         return table
#
#     # ゲームの内容によって手札を変更します
#     @staticmethod
#     def initialCards(gameMode):
#         if gameMode == "21":
#             return 2
#         if gameMode == "poker":
#             return 5
#
#     # 卓の情報を表示するメソッドを作成します。
#     @staticmethod
#     def printTableInformation(table):
#         print("Amount of players: " + str(len(table["players"])) +
#               "... Game mode: " + table["gameMode"] + ". At this table: ")
#
#         for i, player in enumerate(table["players"]):
#             print(str(i + 1) + " player's cards")
#             for card in player:
#                 print(card.getCardString())
#
#     # 各プレーヤーの手札を受け取って、合計値を計算するscore21Individualメソッドを作成します。
#     # ブラックジャックでは値の合計値が21を超えるとNGなのでその場合は0とします。
#     @staticmethod
#     def score21Individual(cards):
#         value = 0
#         for card in cards:
#             value += card.intValue
#         return value if 21 >= value >= 1 else 0
#
#     # ブラックジャックで誰が勝利したか表示する関数を作成します。
#     # それぞれのプレイヤーの手札をscore21Individualで計算し、配列に保存します。例: [10,16,15,16,15,15]
#     # この場合、勝利するプレイヤーが複数存在することから、cache[10] = 1, cache[15] = 3, cache[16] = 2のように書き換えます。
#     # 配列 [10,16,15,16,15,15]の最大値は16で、cache[16] > 1なのでドローになります。
#     # もし、0 <= cache[16] <= 1なら、そのプレイヤーの勝利、それ以外の場合は勝者が誰もいないことになります。
#     # ではこのロジックを関数にしてみましょう。
#     @staticmethod
#     def winnerOf21(table):
#         points = []
#         cache = {}
#         for cards in table["players"]:
#             point = Dealer.score21Individual(cards)
#             # それぞれのpointを配列に保存
#             points.append(point)
#             if point in cache:
#                 cache[point] += 1
#             else:
#                 cache[point] = 1
#         # 各プレーヤーの得点を確認
#         print(points)
#         # print(cache)
#         winnerIndex = HelperFunctions.maxInArrayIndex(points)
#
#         if cache[points[winnerIndex]] > 1:
#             return "It is a draw"
#         elif cache[points[winnerIndex]] >= 0:
#             return "player " + str(winnerIndex + 1) + " is the winner."
#         else:
#             return "No winners.."
#
#     # 卓のゲームの種類によって勝利条件を変更するcheckWinnerというメソッドを作成します。
#     @staticmethod
#     def checkWinner(table):
#         if table["gameMode"] == "21":
#             return Dealer.winnerOf21(table)
#         else:
#             return "no game"
#
#
#
# # 計算のみを行うHelperFunctionsクラスを定義します。
# class HelperFunctions:
#
#     # 数値で構成させる配列を受け取り、最大値のインデックスを返します。
#     @staticmethod
#     def maxInArrayIndex(intArr):
#         maxIndex = 0
#         maxValue = intArr[0]
#         for i, num in enumerate(intArr):
#             if num > maxValue:
#                 maxValue = num
#                 maxIndex = i
#         return maxIndex
#
# table1 = Dealer.startGame(4, "21")
# Dealer.printTableInformation(table1)
# print(Dealer.checkWinner(table1))
#
# table2 = Dealer.startGame(1, "poker")
# Dealer.printTableInformation(table2)
# print(Dealer.checkWinner(table2))




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








