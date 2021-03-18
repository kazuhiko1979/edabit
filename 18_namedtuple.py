from collections import namedtuple

def main():

    Test_Ret = namedtuple('Test_Ret',
                          ('Name', 'English', 'Math'))

    John = Test_Ret(Name='John', English=78, Math=89)
    Mike = Test_Ret(Name='Mike', English=64, Math=94)
    print(John)
    print(Mike)

    print(John.English)
    print(John[0])

    for i in John:
        print(i)

    # John.English = 10

    return

if __name__ == '__main__':
    main()