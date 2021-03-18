from collections import OrderedDict

def main():

    some_dict = {'John':18, 'Paul': 9, 'Mike': 5}
    sort_dict = sorted(some_dict.items(), key=lambda t:t[0])
    print(sort_dict)

    ordr_dict = OrderedDict(sort_dict)
    print(ordr_dict)

    last_elem = ordr_dict.popitem(last=True)
    print(last_elem)
    print(ordr_dict)

    ordr_dict['Paul'] = 10
    print(ordr_dict)

    ordr_dict.move_to_end('John')
    print(ordr_dict)

    ordr_dict.move_to_end('John', False)
    print(ordr_dict)














    return


if __name__ == '__main__':
    main()