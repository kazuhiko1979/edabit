"""
String Match by Two Letters
Create a function that takes two strings, a and b. Return the number of times the two strings contain the same two letters at the same index. The two letters must appear at consecutive indices.

For example, if a = "bboiizz" and b = "bbuiiz", your function should return 3, since the "bb", "ii", and "iz" appear at the same place in both strings.

Examples
str_match_by2char("yytaazz", "yyjaaz") ➞ 3

str_match_by2char("edabit", "ed") ➞ 1

str_match_by2char("", "") ➞ 0
Notes
Don't forget to return the result.
"""

def str_match_by2char(a, b):

  # res_a = [a[i]+a[i+1] for i in range(0, len(str(a))-1)]
  # res_b = [b[j]+b[j+1] for j in range(0, len(str(b))-1)]
  #
  # return sum(a == b for a, b in zip(res_a, res_b))

  num = 0

  for i in range(min(len(a), len(b))-1):
    if a[i:i+2] == b[i:i+2]:
      num += 1
  return num



print(str_match_by2char("yytaazaz", "yyjaaz"))
print(str_match_by2char("edabit", "ed"))
print(str_match_by2char("", ""))
print(str_match_by2char('AABBccDD', 'ABBBjjD'))
print(str_match_by2char('AAjjAAjj', 'iAjjAi'))
print(str_match_by2char('iAjjAi', 'AAjjAAjj'))