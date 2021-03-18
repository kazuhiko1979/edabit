import os

def main():

    # print(os.getcwd())
    # os.mkdir('./SomeDirectory')
    # print(os.path.exists('./SomeDirectory'))
    # os.rmdir("./SomeDirectory")
    # os.remove("./somefile.txt")
    # os.rename("./A.txt", "./B.txt")

    path = r"C:\Users\kazuh\PycharmProjects\edabit"
    file_name = r"SomeFile.txt"

    # print(os.path.basename(path))
    # print(os.path.dirname(path))
    # print(os.listdir(path))
    # print(os.path.splitext(path))

    print(os.path.join(path, file_name))

    return


if __name__ == '__main__':
    main()



