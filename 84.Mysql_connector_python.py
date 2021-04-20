import mysql.connector
import pprint


def get_connection():

    return mysql.connector.connect(user='root',
                                   password='**********',
                                   host='127.0.0.1',
                                   port='3306',
                                   database='some')


def insert(name, age):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = \
        "INSERT INTO `some`.`person` (`name`, `age`) \
        VALUES (%(name)s, %(age)s);"

    param = {
        "name":name,
        "age":age
    }

    cursor.execute(query, param)
    connection.commit()
    print(cursor.statement)

    cursor.close()
    connection.close()


def select_all():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM `some`.`person` LIMIT 1000;"
    cursor.execute(query)
    print(cursor.statement)

    ret_list = []
    for row in cursor:
        ret = {}
        ret["id"] = row["id"]
        ret["name"] = row["name"]
        ret["age"] = row["age"]
        ret_list.append(ret)

    pprint.pprint(ret_list)

    cursor.close()
    connection.close()


def update(name, age):

    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE `some`.`person` \
            SET `age`=%(age)s \
            WHERE `name`=%(name)s);"

    param = {
        "name": name,
        "age": age
    }

    cursor.execute(query, param)
    print(cursor.statement)
    connection.commit()

    cursor.close()
    connection.close()


def delete(name):

    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM `some`.`person` \
            WHERE `name`=%(name)s);"

    param = {
        "name": name
    }

    cursor.execute(query, param)
    connection.commit()
    cursor.close()
    connection.close()



def main():

    # insert("John", 41)
    # insert("Mike", 46)
    # insert("Paul", 33)
    #
    # select_all()

    # update("John", 32)
    # delete("Mike")

    select_all()

    return


if __name__ == "__main__":
    main()



