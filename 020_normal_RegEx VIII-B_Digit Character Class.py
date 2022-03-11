"""
文字列のすべての非数字文字に一致する正規表現を記述します。

正規表現:Regular expression
文字列内で文字の組み合わせを照合するために用いられるパターン
正規表現の条件に合致した文字の組み合わせのみ表現する方法(re.findallを活用）

参考サイト：
https://www.w3schools.com/python/python_regex.asp

例題：
txt = "242Python2345can3443be3254324addictive!"
pattern = "yourregularexpressionhere"

" ".join(re.findall(pattern, txt)) ➞ "Python can be addictive!"

備考：
関数ではなく、パターンを作成してください。
”re” をインポートしてください。
"""

import re

txt = "242Python2345can3443be3254324addictive!"
# pattern = '\D+'
pattern = '[A-z!?.,]+'

print(" ".join(re.findall(pattern, txt)))




































# """
# Write the regular expression that will match all non-digit characters of a string.
# Use the character class \D in your expression.
#
# Example
# txt = "242Python2345can3443be3254324addictive!"
# pattern = "yourregularexpressionhere"
#
# " ".join(re.findall(pattern, txt)) ➞ "Python can be addictive!"
# Notes
# You don't need to write a function, just the pattern.
# Do not remove import re from the code.
# """
#
#
#
# import re
#
# txt = "242Edabit2345can3443be3254324addictive!"
#
#
# # [a-z\d]は英数字のうち任意の一文字を意味します。
# #\d	Returns a match where the string contains digits (numbers from 0-9)
# # pattern = '\d'
#
# # \D	Returns a match where the string DOES NOT contain digits
# # pattern = '\D+'
#
# # [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
# # pattern = "[A-z!?.,]+"
#
# # pattern = "[A-z!?.,]+\D"
#
# print(" ".join(re.findall(pattern, txt)))

