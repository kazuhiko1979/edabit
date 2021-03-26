import configparser


def main():

    config = configparser.ConfigParser()
    config.read('C\config.ini', 'UTF-8')

    # print(config.get('server', 'ip'))
    # print(config.get('server', 'port'))
    # print(config.get('server', 'host'))

    with open('C\some.ini', 'w') as f:
        config.write(f)

    return

if __name__ == '__main__':
    main()