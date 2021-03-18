from pathlib import Path

def main():

    # カレントディレクトリ取得
    # p = Path(Path.cwd())

    # some_dir = Path(r"C:\Users\kazuh\PycharmProjects\edabit\C")

    # HomeDir
    # print(Path.home())
    # print(p)
    #
    # print("p.parent :", p.parent) # 親ディレクトリ
    # print("p.name :", p.name) # Dir名

    # 親要素の配列
    # print(p.parents)
    # for i in p.parents:
    #     print(i)

    # print(p)
    # print("p.exists:", p.exists())
    # print("p.is_dir", p.is_dir())
    # print("p.is_file", p.is_file())
    #

    # some_dir = Path(r"C:\Users\kazuh\PycharmProjects\edabit\Some")
    # some_dir.mkdir(parents=True, exist_ok=True)
    # some_dir.rmdir()

    # print(list(some_dir.glob('**/*.txt')))
    #
    # for i in some_dir.glob('**/*.txt'):
    #     print(i)
    #
    # some_dir = Path(r"./") # 絶対パス変換
    # print(some_dir)
    # print(some_dir.resolve())


    some_file = Path(r"A1.txt")
    # print(some_file)
    with some_file.open() as f:
        print(f.readline())


    return


if __name__ == '__main__':
    main()