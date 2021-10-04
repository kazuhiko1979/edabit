"""
ブラックジャック
easy
Jimmy はカジノでブラックジャックを行いました。Jimmy の手札 playerCards、
ディーラーの手札 houseCards が与えられるので、Jimmy が勝利した場合 true、
ディーラーが勝利した場合 false を返す、winnerBlackjack という関数を定義してください。条件は以下の通りです。


- カードはマークと値によって構成されています。

　
- カードの値は、A = 1、2-10 はそのままの値、J = 11、Q = 12、K = 13 とします。

　
- プレイヤーの手札の合計値が 21 を超えている場合はプレイヤーの敗北となります。

- ディーラーの手札の合計値が 22 未満でかつプレイヤーのカードの合計値より大きければ、プレイヤーの敗北となります。

- ドローだった場合はプレイヤーの敗北となります。

関数の入出力例

入力のデータ型： string[] playerCards, string[] houseCards

出力のデータ型： bool

winnerBlackjack(["♣4","♥7","♥7"],["♠Q","♣J"]) --> true

winnerBlackjack(["♥10","♥6","♣K"],["♠Q","♦2","♥K"]) --> false

winnerBlackjack(["♠3","♠J","♣5"],["♣A","♥Q","♣5"]) --> true

winnerBlackjack(["♥2","♣A","♣8","♥7","♥3"],["♥6","♥K","♣5","♥K"]) --> true

winnerBlackjack(["♥2","♣A","♣8","♥7","♥3"],["♥2","♣A","♣8","♥7","♥3"]) --> false

"""
def winnerBlackjack(playerCards, houseCards):
    playerScore = 0
    houseScore = 0

    # プレイヤーのカードの合計値を計算
    for card in playerCards:
        playerScore += cardValue(card)
    for card in houseCards:
        houseScore += cardValue(card)

    # プレイヤーのスコアが21を超えている場合、あるいはドローの場合、false
    if playerScore > 21 or playerScore == houseScore:
        return False
    if houseScore < 22 and houseScore > playerScore:
        return False
    return True


def cardValue(cardString):
    string = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    # 数字だけを切り取り、配列のどこに存在するかを返す
    # 例えば、Kの場合、index=12が返されます。Aの場合、index=0が返されます。
    return string.index(cardString[1:]) + 1


# def winnerBlackjack(playerCards, houseCards):

#     # playerCardsの得点とhouseCardsの得点を取得する
#     playerCards = [i[1:] for i in playerCards]
#     houseCards = [i[1:] for i in houseCards]
#
#     return compareScores(playerCards, houseCards)
#
# def compareScores(list_playerScore, list_houseScore):
#
#     # - カードの値は、A = 1、2-10 はそのままの値、J = 11、Q = 12、K = 13 とします。
#     mark_score = {
#         'A': 1,
#         'J': 11,
#         'Q': 12,
#         'K': 13
#     }
#
#     player = sum([int(mark_score[i]) if i in mark_score.keys() else int(i) for i in list_playerScore])
#     house = sum([int(mark_score[i]) if i in mark_score.keys() else int(i) for i in list_houseScore])
#
#     if player == house or player > 21:
#         return False
#     elif house < 22 and house > player:
#         return False
#     else:
#         return True

print(winnerBlackjack(["♣4", "♥7", "♥7"], ["♠Q", "♣J"]))
print(winnerBlackjack(["♥10","♥6","♣K"],["♠Q","♦2","♥K"]))
print(winnerBlackjack(["♠3","♠J","♣5"],["♣A","♥Q","♣5"]))
print(winnerBlackjack(["♥2","♣A","♣8","♥7","♥3"],["♥6","♥K","♣5","♥K"]))
print(winnerBlackjack(["♥2","♣A","♣8","♥7","♥3"],["♥2","♣A","♣8","♥7","♥3"]))

