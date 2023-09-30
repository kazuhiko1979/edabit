"""
Give Me a Hint
Given a sentence, return a list of strings which gradually reveals the next letter in every word at the same time. Use underscores to hide the remaining letters.

Examples
grant_the_hint("Mary Queen of Scots") ➞ [
  "____ _____ __ _____",
  "M___ Q____ o_ S____",
  "Ma__ Qu___ of Sc___",
  "Mar_ Que__ of Sco__",
  "Mary Quee_ of Scot_",
  "Mary Queen of Scots"
]

grant_the_hint("The Life of Pi") ➞ [
  "___ ____ __ __",
  "T__ L___ o_ P_",
  "Th_ Li__ of Pi",
  "The Lif_ of Pi",
  "The Life of Pi"
]
"""

def grant_the_hint(txt):
    words = txt.split()
    max_length = max(len(word) for word in words)
    result = []

    for i in range(max_length + 1):
        hint = " ".join(word[:i] + "_" * (len(word) - i) for word in words)
        result.append(hint)

    return result

# テストケース
print(grant_the_hint('The River Nile'))
print(grant_the_hint("Mary Queen of Scots"))
print(grant_the_hint("The Life of Pi"))


# def grant_the_hint(txt):
#   words = txt.split()
#   m = max(len(w) for w in words) + 1
#   return [' '.join(w[:i] + '_'*(len(w)-i) for w in words) for i in range(m)]


# def grant_the_hint(txt):

# 	temp = txt.split()
# 	start = 1
# 	end = 1
# 	sub = []
# 	result = []
# 	top = ' '.join(['_' * len(word) for word in txt.split()])
# 	result.append(top)
# 	buttom = ''

# 	while buttom != txt:
# 		for word in txt.split():
# 			if len(word) - end:
# 				word = word[:start] + '_' * (len(word) - end)
# 				sub.append(word)
# 				if len(sub) == len(temp):
# 					result.append(' '.join(sub))
# 					sub = []
# 					start += 1
# 					end += 1
# 					buttom = result[-1]
# 					break
# 			else:

# 				sub.append(word)
# 				if len(sub) == len(temp):
# 					result.append(' '.join(sub))
# 					sub = []
# 					start += 1
# 					end += 1
# 					buttom = result[-1]
# 					break
# 	return result

# print(grant_the_hint('The River Nile'))
# print(grant_the_hint("Mary Queen of Scots"))
# print(grant_the_hint("The Life of Pi"))
