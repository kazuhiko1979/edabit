"""
Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:

"nines:your answer, threes:your answer, ones:your answer"
You need to find out how many ones, threes, and nines it would at least take for the number of each to add up to the given integer when multiplied by one, three or nine (depends).

Examples
ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"

ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"

ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"
"""


class ones_threes_nines:

    def __init__(self, num):
        self.nines = num // 9
        self.threes = (num - self.nines*9) // 3
        self.ones = num - ((self.nines * 9) + (self.threes * 3))
        self.answer = 'nines:{}, threes:{}, ones:{}'.format(
            self.nines, self.threes, self.ones)

print(ones_threes_nines(10).answer)
print(ones_threes_nines(22).answer)
print(ones_threes_nines(15).answer)
print(ones_threes_nines(1).answer)

