"""
There are three towers. The objective of the game is to move all the disks over to tower #3, but you can't place a larger disk onto a smaller disk. To play the game or learn more about the Tower of Hanoi, check the Resources tab.
Tower of Hanoi
Create a function that takes a number discs as an argument and returns the minimum amount of steps needed to complete the game.

Examples
tower_hanoi(3) ➞ 7
tower_hanoi(5) ➞ 31
tower_hanoi(0) ➞ 0
Notes
The amount of discs is always a positive integer.
"""
# Recursive Python function to solve tower of hanoi


class count:
    """
    カウントのためのクラス
    """
    def __init__(self, func):
        self.count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@count
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):

    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return

    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


n = 3

TowerOfHanoi(n, 'A', 'C', 'B')
print("Move count", TowerOfHanoi.count)

# def tower_hanoi(discs):
#
#      return 2 ** discs - 1
#
# print(tower_hanoi(3))
# print(tower_hanoi(5))