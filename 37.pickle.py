import pickle


class SomeClass(object):

    def __init__(self, msg):
        self.msg = msg
        self.file = open('test.txt', mode='r')

    def say(self):
        print(self.msg)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['file']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.file = open("test.txt", mode='r')
        print(self.file.read())


def main():

    # with open('C\some.pickle', mode='wb') as f:
    #     pickle.dump('Hello World', f)

    # with open('C\some.pickle', mode='rb') as f:
    #     print(pickle.load(f))

    obj = SomeClass('I am SomeClass!!!')

    with open('C\some.pickle', mode='wb') as f:
        pickle.dump(obj, f)

    with open('C\some.pickle', mode='rb') as f:
        obj = pickle.load(f)
        obj.say()



    return

if __name__ == '__main__':
    main()

