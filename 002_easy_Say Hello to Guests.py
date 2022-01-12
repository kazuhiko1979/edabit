"""
レベル：やさしい

namea
①名前のリストを取得します。
②各名前の前に「Hello」を追加します
③挨拶分1つの文字列として返します。
④「Hello　名前」の間にコンマを入れた1つの文字列である必要があります。

例
greet_people(["Joe"]) ➞ "Hello Joe"

greet_people(["Angela", "Joe"]) ➞ "Hello Angela, Hello Joe"

greet_people(["Frank", "Angela", "Joe"]) ➞ "Hello Frank, Hello Angela, Hello Joe"
"""

def greet_people(names):

    # リスト内法表記
    return ", ".join(["Hello {} ".format(name) for name in names])


    # greeting = []
    #
    # for name in names:
    #     name = "Hello " + name
    #     greeting.append(name)
    # return ", ".join(greeting)


print(greet_people(["Joe"]))
print(greet_people(["Angela", "Joe"]))




















# """
# In this exercise you will have to:
#
# Take a list of names.
# Add "Hello" to every name.
# Make one big string with all greetings.
# The solution should be one string with a comma in between every "Hello (Name)".
#
# Examples
# greet_people(["Joe"]) ➞ "Hello Joe"
#
# greet_people(["Angela", "Joe"]) ➞ "Hello Angela, Hello Joe"
#
# greet_people(["Frank", "Angela", "Joe"]) ➞ "Hello Frank, Hello Angela, Hello Joe"
# """
#
#
# def greet_people(names):
#
#     return ', '.join(["Hello {}".format(name) for name in names])
#
#
# print(greet_people(["Joe"]))
# print(greet_people(["Angela", "Joe"]))
# print(greet_people(["Frank", "Angela", "Joe"]))