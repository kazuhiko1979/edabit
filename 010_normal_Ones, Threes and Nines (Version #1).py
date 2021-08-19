"""
Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class.
You will make variables (self.ones, self.threes, self.nines) to do this.

Examples
n1 = ones_threes_nines(5)
n1.nines ➞ 0

n1.ones ➞ 5

n1.1threes ➞
Notes
Do not use the math module.
See version #2 of this series.
"""

class ones_thress_nines:

    def __init__(self, num):
        self.ones = num
        self.threes = num // 3
        self.nines = num // 9

    # def __init__(self, num):
    #
    #     self.num = num
    #
    # @property
    # def ones(self):
    #     return self.num
    #
    # @property
    # def threes(self):
    #     return self.num // 3
    #
    # @property
    # def nines(self):
    #     return self.num // 9

n1 = ones_thress_nines(5)
print(n1.ones)
print(n1.threes) # 5 // 3 = 1
print(n1.nines)  # 5 // 9 = 0













