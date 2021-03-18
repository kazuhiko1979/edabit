import timeit


def process():

    ret = []
    for i in range(20000000):
        ret.append(i)


def main():

    print(timeit.timeit(process, number=1))

    return

if __name__ == '__main__':

    main()

# def func():
#
#     ret = []
#     for i in range(100):
#         ret.append(i)