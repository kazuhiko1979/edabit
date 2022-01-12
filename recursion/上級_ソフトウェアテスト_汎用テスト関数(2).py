"""
汎用テスト関数(2)
equalAssertion 関数は、2 つのデータが等しいかどうかをチェックする方法の1つに過ぎません。a == b のケースだけでなく、
データの範囲をテストしたり、大小比較等の比較ロジックを適用したい場合もあるでしょう。

入力や出力が有効であることをテストすることは重要であり、これはデータ検証と呼ばれます。
通常、これらの述語はその場で構築されるか、定義済みの関数が再利用されます。

では、データと述語を受け取る、より汎用的なアサーションを構築してみましょう。
多くのアプリケーションで使われる、与えられた文字列がメールであるかどうかチェックするテストを見てみましょう。
"""

def assertionTest(a, callback):

    result = callback(a)
    print(f"checking againt {str(a)}, is it valid?...{result}")
    assert result
    return True

# emailが有効かテストする述語
# 有効なemailとは空白のスペースがなく、@を含み、@の後に.が含まれる文字列を指します。
def isValidEmail(email):
    if email.find(" ") >= 0 or email.find("@") == -1 \
        or email[email.find("@")+1:
           len(email)].find("@") != -1:
        return False
    if email[email.find("@") + 1:
       len(email)].find(".") == -1:
        return False
    return True

assertionTest("johnnyTest@test.com", isValidEmail)
assertionTest("John@Test", isValidEmail)




