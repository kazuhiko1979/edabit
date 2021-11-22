"""
Create a function that takes a list of integers that represent the amount in dollars that a single stock is worth, and return the maximum profit that could have been made by buying stock on day x and selling stock on day y where y>x.

If given the following list:

[44, 30, 24, 32, 35, 30, 40, 38, 15]
... your program should return 16 because at index 2 the stock was worth $24 and at the index 6 the stock was then worth $40, so if you bought the stock at 24 and sold it on 40, you would have made a profit of $16, which is the maximum profit that could have been made with this list of stock prices.

If there is no profit that could have been made with the stock prices, then your program should return -1 (e.g. [[10, 9, 8, 2]] should return -1).

Examples
stock_picker([10, 12, 4, 5, 9]) ➞ 5

stock_picker([14, 20, 4, 12, 5, 11]) ➞ 8

stock_picker([80, 60, 10, 8]) ➞ -1
"""

def stock_picker(lst):

    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] - lst[i] > 0:
                res.append(lst[j] - lst[i])
    return max(*res) if len(res) != 0 else -1

    # if not lst:
    #     return 0
    #
    # mini = lst[0]
    # rec = 0
    #
    # for val in lst[1:]:
    #     rec = max(rec, val - mini)
    #     mini = min(mini, val)
    # return rec or -1





    # current_index = 0
    # next_index = 1
    # profit = []
    # temp_profit = 0
    #
    # while current_index <= len(lst):
    #
    #     if next_index < len(lst):
    #         current_value = lst[current_index]
    #
    #         if current_value < max(lst[next_index:]):
    #             temp_profit = (max(lst[next_index:]) - current_value)
    #             profit.append(temp_profit)
    #             current_index += 1
    #             next_index += 1
    #         else:
    #             current_index += 1
    #             next_index += 1
    #     else:
    #         return max(profit) if profit != [] else -1


print(stock_picker([10, 12, 4, 5, 9]))
print(stock_picker([14, 20, 4, 12, 5, 11]))
print(stock_picker([80, 60, 10, 8]))
print(stock_picker([90, 100, 111, 0, 1, 2, 3]))
print(stock_picker([1, 2, 4, 10, 100, 2, 3]))
print(stock_picker([10, 1000, 1, 1, 1, 2000, 3]))
print(stock_picker([7, 1, 5, 5, 2, 1, 3]))
print(stock_picker([100, 10, 8, 5]))
#



