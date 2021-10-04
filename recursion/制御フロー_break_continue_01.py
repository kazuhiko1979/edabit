"""
breakとcontinue
反復ループを使うとき、強制的に反復から離脱させる break キーワードというものがあります。
制御フロー内で break キーワードが処理されると、反復ループから抜け出すことができます。
この break キーワードはループ内で条件が満たされた場合に使用されるため、
コンピュータが不要な計算をしなくて済むようになります。
では、文字列の中から文字を探す場合を見てみましょう。
文字が見つかったら残りの文字列の処理を続ける必要はないので、
ループから抜け出すことができます。
"""

def findLetter(sentence, letter):

    found = False
    message = "Will we find [" + letter + "] in our message? "

    for i in range(0, len(sentence)):
        # 文字が文章の中で発見されたとき、found変数をtrueにし、for loopから離脱します。
        if sentence[i] == letter[0]:
            found = True
            break
    return message + "It look like we found it!" if found else message + "Sadly, we did not find it."

print(findLetter("It is a sunny day.", "a"))
print(findLetter("It is a sunny day.", "o"))

"""
数値 x と y を受け取り、x の各桁が y に近いかどうか記録する関数を作成してみましょう
各桁が y と同じである、1 離れている、2 以上離れている場合に分けて、それぞれカウントしていきます。
"""
import math

# 数字とラッキーナンバー（0～9)を取得します。

def luckyDigitRange(number, luckyDigit):

    perfectCounter = 0
    closeCounter = 0
    closeEnoughCounter = 0

    message = "Let's see how well our digits match with " + str(luckyDigit) + "...."

    # 桁が存在する限り、処理を続けます。
    while number >= 1:
        # 最後の桁を取得
        currentDigit = number % 10
        # 数字から最初の数字を取り除く
        number = math.floor(number / 10)

        distance = abs(currentDigit - luckyDigit)

        # 桁の数字がラッキーナンバーと2以上離れている場合、次のループに進みます。
        if distance > 2:
            continue

        if distance == 0:
            perfectCounter = perfectCounter + 1
        elif distance == 1:
            closeCounter = closeCounter + 1
        else:
            closeEnoughCounter = closeEnoughCounter + 1

    return message + " Perfect digits: " + str(perfectCounter) + \
        " - Close: " + str(closeCounter) + " - Close Enough: " + str(closeEnoughCounter)

print(luckyDigitRange(575445677589, 7))


















