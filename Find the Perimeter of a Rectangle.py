# find_perimeter(6, 7) ➞ 26
# find_perimeter(20, 10) ➞ 60
# find_perimeter(2, 9) ➞ 22

def find_perimeter(length, width) -> int:

    perimeter = (length + width) * 2
    return print(perimeter)


if __name__ == '__main__':
    find_perimeter(6, 7)
    find_perimeter(20, 10)
    find_perimeter(2, 9)

