import glob

def main():
    # ワイルドカードファイル検索

    # print(glob.glob('*.txt'))
    # print(glob.glob('*[0-9].*'))
    print(glob.glob('C:/test/*.txt', recursive=True))



    return

if __name__ == '__main__':
    main()
