from argparse import ArgumentParser
import sys


def main():

    # parser = ArgumentParser()
    #
    # parser.add_argument(
    #     '-n', '--number',
    #     type=int,
    #     dest='number',
    #     required=True,
    #     help='処理の回数'
    # )
    # parser.add_argument(
    #     '-s', '--string',
    #     type=str,
    #     dest='string',
    #     required=True,
    #     help='表示文字列'
    # )
    #
    # args = parser.parse_args()

    # for i in range(args.number):
    #     print(str(i)+':'+args.string)
    #
    # return

    print(sys.argv[1])

    return

if __name__ == '__main__':
    main()