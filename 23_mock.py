from mock import Mock

class DB():
    def select_name(self):
        return 'I am database.'

def main():

    db = DB()
    # print(db.select_name())

    # db.select_name = Mock()
    # db.select_name.return_value = 'I am Mock'
    # db.select_name = Mock(return_value='I am database.')
    # print(db.select_name())
    #
    # # UnitTest
    # if db.select_name() == 'I am database.':
    #     print('Test OK.')
    # else:
    #     print("Test NG")

    # mock = Mock(side_effect=Exception('DB Error'))
    # mock()

    mock = Mock(side_effect=[1, 2, 4, 16])

    if mock() == 1:
        print("Test OK")
    if mock() == 2:
        print("Test OK")
    if mock() == 3:
        print("Test OK")

    return

if __name__ == '__main__':
    main()