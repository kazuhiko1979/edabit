from tinydb import TinyDB, Query
import pprint

def main():

    db = TinyDB('Some.json')
    query = Query()

    # 初期化
    db.purge()

    db.insert({'name':'John', 'age':26})
    db.insert({'name':'Mike', 'age':22})

    dict_list = [{'name':'Bob', 'age':25},
                 {'name':'Paul', 'age':40}]
    db.insert_multiple(dict_list)

    pprint.pprint(db.all())

    # Search
    print("-----")
    pprint.pprint(db.search(query.age <= 25))

    # update
    print("-----")
    db.update({'age':27}, query.name == 'John')
    print("-----")
    pprint.pprint(db.all())

    # remove
    db.remove(query.age <= 25)
    print("-----")
    pprint.pprint(db.all())





    return


if __name__ == "__main__":

    main()