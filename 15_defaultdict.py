from collections import defaultdict


def init():
    return 10

def main():

    # some_str = "fiafjoajfoareiafahfuafvae"
    # print(some_str)

    # some_dict = {}
    # for key in some_str:
    #     if key not in some_dict:
    #         some_dict[key] = 0
    #     some_dict[key] += 1
    # print(some_dict)

    # some_dict = defaultdict(lambda : 0)
    # some_dict = defaultdict(int)
    #
    # for key in some_str:
    #     some_dict[key] += 1
    # print(dict(some_dict))


    test_ret = {'John':{'English':78, 'Math':65, 'History':45},\
                'Paul':{'English':82,            'History':85},\
                'Mike':{'English':42, 'Math':69,             }}

    # each_total = {}
    # for someone in test_ret:
    #     for subject in test_ret[someone]:
    #         if subject not in each_total:
    #             each_total[subject] = test_ret[someone][subject]
    #             continue
    #         each_total[subject] += test_ret[someone][subject]
    # print(each_total)

    each_total = defaultdict(int)
    for someone in test_ret:
        for subject in test_ret[someone]:
            each_total[subject] += test_ret[someone][subject]
    print(each_total)


    return


if __name__ == '__main__':
    main()

