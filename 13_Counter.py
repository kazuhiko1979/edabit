from collections import Counter


def main():

    # name_list = ['Paul', 'Paul', 'Mike', 'Paul', 'Mike', 'John', 'Paul','Paul', 'Mike','Mike']
    # ret = Counter(name_list)
    #
    # print(ret)
    #
    # print(ret['Paul'])
    #
    # print(len(ret))
    #
    # print(ret.most_common())
    #
    # print(ret.most_common()[0])
    # print(ret.most_common()[1])
    # print(ret.most_common()[2])
    # print(ret.most_common()[0][0])
    # print(ret.most_common()[0][1])

    sentence = "Plutarch remarked the fact that the Greek myths of Cronus, of Dionysus, of Apollo and the Python, and of Demeter, all the things that are shrouded in mystic ceremonies and are presented in rites," " do not fall short in absurdity of the legends about Osiris and Typhon."
    word_list = sentence.split()
    ret = Counter(word_list)

    print(ret)

    return

if __name__ == '__main__':
    main()


