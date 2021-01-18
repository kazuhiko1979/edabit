# remainder(1, 3) ➞ 1
# remainder(3, 4) ➞ 3
# remainder(5, 5) ➞ 0
# remainder(7, 2) ➞ 1
def remainder(x, y):
    num = x % y
    return num


if __name__ == '__main__':
    print(remainder(1, 3))
    print(remainder(3, 4))
    print(remainder(5, 5))
    print(remainder(7, 2))
