"""
tri_area(3, 2) ➞ 3
tri_area(7, 4) ➞ 14
tri_area(10, 10) ➞ 50
"""
def tri_area(base: int, height: int) -> int:
    area = (base * height) / 2
    return print(int(area))


if __name__ == '__main__':
    tri_area(3, 2)
    tri_area(7, 4)
    tri_area(10, 10)


