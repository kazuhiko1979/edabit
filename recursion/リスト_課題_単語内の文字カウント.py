"""
単語内の文字カウント
Herbie は小学生向けに英語のゲームを作りました。
単語が入っているバッグを用意し、
単語の中に含まれる特定のアルファベットをカウントしていくというものです。
単語のリスト bagOfWords とアルファベット keyCharacter が与えられるので、
単語の中に特定のアルファベットが何回現れるかを返す、
charInBagOfWordsCount という関数を定義してください。

入力のデータ型： string[] bagOfWords, char keyCharacter
出力のデータ型： integer
"""


def charInBagOfWordsCount(bagOfWords, keyCharacter):

    count = 0
    for words in bagOfWords:
        for word in words:
            if keyCharacter in word:
                count += 1
    return count

print(charInBagOfWordsCount(["hello", "world"], "o"))
print(charInBagOfWordsCount(["hello","world"],"p"))
print(charInBagOfWordsCount(["The","tech","giant","is in the","city center"],"p"))
print(charInBagOfWordsCount(["The","tech","giant","is in the","city center"],"e"))