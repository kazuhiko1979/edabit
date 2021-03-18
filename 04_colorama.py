from colorama import init
from colorama import Fore, Back, Style

def main():

    init()

    print(Fore.RED + '赤いテキストです')
    print(Back.GREEN + '緑の背景にします')
    print(Style.RESET_ALL)
    print('通常表示に戻りました')
    print("協調したい" + Back.RED + "文字列" + Back.BLACK + "です")
    print(Style.RESET_ALL)

    return


if __name__ == '__main__':
    main()