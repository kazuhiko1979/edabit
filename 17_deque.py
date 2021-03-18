from collections import deque


def main():

    str = 'abcdefghi'
    # str_list = []
    d = deque('abcdefghi')
    # for i in str:
    #     str_list.append(''.join(i))
    # print(str_list)
    print(d)
    d.append("j")
    print(d)

    d.appendleft("0")
    print(d)

    print(d.count("a"))

    d.extend("klmn")
    print(d)

    print(d.index("b", 0, 10))

    d.insert(10, "z")
    print(d)

    print(d.pop())
    print(d)

    d.remove("e")
    print(d)

    d.reverse()
    print(d)

    d.reverse()
    print(d)

    d.rotate(2)
    print(d)

    print(list(d))

    return

if __name__ == '__main__':
    main()