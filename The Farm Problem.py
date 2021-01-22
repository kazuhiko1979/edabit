"""
chickens = 2 legs
cows = 4 legs
pigs = 4 legs

Output ->
animals(2, 3, 5) ➞ 36
animals(1, 2, 3) ➞ 22
animals(5, 2, 8) ➞ 50
"""
def animals(chikens, cows, pigs) -> int:
    chicken_legs = 2
    cow_legs = 4
    pig_legs = 4
    total_legs = (chikens * chicken_legs) + (cows * cow_legs) + (pigs * pig_legs)
    return total_legs


if __name__ == '__main__':
    print(animals(2, 3, 5))
    print(animals(1, 2, 3))
    print(animals(5, 2, 8))




