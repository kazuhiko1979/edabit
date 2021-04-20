import numpy as np


def main():

    # a = np.arange(10)
    # print(a)
    # print(a[4])
    # print(a[4:7])

    # a = np.array([[1, 2, 3], [4, 5, 6]])
    # print(a)
    # print(a[1, 1])
    # print(a[0, 0])

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = np.hstack((a, b))
    print(c)
    d = np.vstack((a, b))
    print(d)

    # print(np.random.randn())
    # print(np.random.rand())

    # print(np.random.randn(3, 3))

    # a = np.array([[1, 2, 3], [4, 5, 6]])
    # print(a)
    # print(a.sum())
    # print(np.sum(a, axis=0))
    # print(np.sum(a, axis=1))
    #
    # print(a.reshape(3, 2))
    # print(a.T)
    # print(np.transpose(a))






    # print(type(a))
    # print(a)
    # print(list(a))
    # print(a*3)
    # print(a+3)
    # print(a*b)
    # print(a+b)

    # 1*4, 2*5, 3*6
    # print(np.dot(a,b))
    #
    # print(np.arange(10))
    # print(np.arange(0, 10, 2))
    # print(np.linspace(1, 10, 100))





    return


if __name__ == "__main__":

    main()