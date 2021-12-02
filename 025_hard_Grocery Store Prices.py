"""
Grocery Store Prices
You are given a list of strings consisting of grocery items, with prices in parentheses. Return a list of prices in float format.

Examples
get_prices(["salad ($4.99)"]) ➞ [4.99]

get_prices([
  "artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"
])

➞ [1.99, 5.99, 0.75]

get_prices([
  "ice cream ($5.99)",
  "banana ($0.20)",
  "sandwich ($8.50)",
  "soup ($1.99)"
])

➞ [5.99, 0.2, 8.50, 1.99]
Notes
See if you can use RegExp to solve (but it's not necessary).
"""
import re

def get_prices(lst):

    return [float(''.join(re.findall('[0-9.]', x))) for x in lst]


    # p = r'(?<=\$)[\d\.]+'
    # return [float(re.search(p, x).group()) for x in lst]


    # res = []
    # for txt in lst:
    #     for char in txt:
    #         if char == '$':
    #             startIndexOfCurrency = txt.index(char)
    #             res.append(float(txt[startIndexOfCurrency+1:-1]))
    # return res

print(get_prices(["salad ($4.99)"]))
print(get_prices([
  "artichokes ($1.99)",
  "rotiserrie chicken ($5.99)",
  "gum ($0.75)"
]))
print(get_prices(['ice cream ($5.99)', 'banana ($0.20)', 'sandwich ($8.50)', 'soup ($1.99)']))
print(get_prices(['pizza ($2.99)', 'shampoo ($15.75)', 'trash bags ($15.00)']))


