# how_many_seconds(2) ➞ 7200
# how_many_seconds(10) ➞ 36000
# how_many_seconds(24) ➞ 86400

def how_many_second(hours):
    seconds = hours * (60**2)
    return seconds


if __name__ == '__main__':
    print(how_many_second(2))
    print(how_many_second(10))
    print(how_many_second(24))

