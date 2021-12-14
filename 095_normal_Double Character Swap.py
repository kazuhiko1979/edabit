"""
Double Character Swap
Write a function to replace all instances of character c1 with character c2 and vice versa.

Examples
double_swap("aabbccc", "a", "b") ➞ "bbaaccc"

double_swap("random w#rds writt&n h&r&", "#", "&")
➞ "random w&rds writt#n h#r#"

double_swap("128 895 556 788 999", "8", "9")
➞ "129 985 556 799 888"
Notes
Both characters will show up at least once in the string.
"""

def double_swap(txt, c1, c2):

  dct = {c1: c2, c2:c1}

  res = []

  for x in txt:
    if x in dct:
      res.append(dct[x])
    else:
      res.append(x)
  return ''.join(res)


  # res = []
  #
  # for i in txt:
  #   if i == c1:
  #     i = i.replace(i, c2)
  #     res.append(i)
  #     continue
  #   if i == c2:
  #     i = i.replace(i, c1)
  #     res.append(i)
  #     continue
  #   else:
  #     res.append(i)
  # return ''.join(res)

print(double_swap("aabbccc", "a", "b"))
print(double_swap("random w#rds writt&n h&r&", "#", "&"))
print(double_swap("128 895 556 788 999", "8", "9"))