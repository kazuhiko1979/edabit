import sqlite3

def main():

    db_name = "Some.db"

    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Create
    # create_table = \
    #     "create table persons (id int, name varchar(64), age int)"
    # cursor.execute(create_table)
    #
    # sql = "insert into persons (id, name, age) values (?, ?, ?)"
    # person = (1, "John", 22)
    # cursor.execute(sql, person)
    #
    # sql = "insert into persons (id, name, age) values (?, ?, ?)"
    # persons = [
    #     (2, "Mike", 26),
    #     (3, "Paul", 24),
    # ]
    # cursor.executemany(sql, persons)
    # connection.commit()

    # update
    # print("-------")
    # sql = "update persons set age='23' where name='John'"
    # cursor.execute(sql)
    # connection.commit()

    # Delete
    print("-------")
    sql = "delete from persons where name='Paul'"
    cursor.execute(sql)
    connection.commit()


    # Select
    sql = "select * from persons"
    for row in cursor.execute(sql):
        print(row)

    connection.close()



    return


if __name__ == '__main__':
    main()