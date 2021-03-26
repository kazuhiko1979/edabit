import dill


class SomeClass(object):

    def __init__(self, msg):
        self.msg = msg
        self.file = open("test.txt", mode='r')

    def say(self):
        print(self.msg)


def main():

    # obj = SomeClass("I am SomeClass2!")
    #
    # with open("some.pickle", "wb") as f:
    #     dill.dump(obj, f)

    with open("Some.pickle", "rb") as f:
        obj = dill.load(f)
        obj.say()
        print(obj.file.read())

    return

if __name__ == '__main__':
    main()

