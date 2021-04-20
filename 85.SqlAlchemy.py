# SQLAlchemy
# Pythonで動作するORM（Object Relational Mapper）
# 接続先情報を変更することで、様々なタイプのDBを扱うことができる
# SQLite, Postgresql, MySQL, Oracle, MS-SQL, etc
# pip install sqlalchemy

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import traceback
import pymysql

Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(50))
    age = sqlalchemy.Column(sqlalchemy.Integer)


def get_db_url():
    db_user = "root"
    db_pswd = "midori1021"
    db_server = "localhost"
    db_port = "3306"
    db_db = "some"

    return "mysql+pymysql://" + \
           db_user + ":" + \
           db_pswd + "@" + \
           db_server + ":" + \
           db_port + "/" + \
           db_db + \
           "?charset=UTF8MB4"


def get_someone(name):
    try:
        engine = sqlalchemy.create_engine(get_db_url(), echo=False)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        session = Session()

        someone = session.query(Person) \
            .filter(Person.name == name) \
            .one()

        print(someone.id)
        print(someone.name)
        print(someone.age)

    except:
        traceback.print_exc()

    finally:
        session.close()


def get_everybody():
    try:
        engine = sqlalchemy.create_engine(get_db_url(), echo=False)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        session = Session()

        everybody = session.query(Person).all()

        for someone in everybody:
            print("------")
            print(someone.id)
            print(someone.name)
            print(someone.age)

    except:
        traceback.print_exc()

    finally:
        session.close()


def add_someone(name, age):
    try:
        engine = sqlalchemy.create_engine(get_db_url(), echo=False)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        session = Session()

        someone = Person(name=name, age=age)
        session.add(someone)
        session.commit()

    except:
        traceback.print_exc()

    finally:
        session.close()


def update_someone(name, age):
    try:
        engine = sqlalchemy.create_engine(get_db_url(), echo=False)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        session = Session()

        someone = session.query(Person) \
            .filter(Person.name == name) \
            .one()

        someone.age = age

        session.add(someone)
        session.commit()

    except:
        traceback.print_exc()

    finally:
        session.close()


def delete_someone(name):
    try:
        engine = sqlalchemy.create_engine(get_db_url(), echo=False)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        session = Session()

        someone = session.query(Person) \
            .filter(Person.name == name) \
            .one()

        session.delete(someone)
        session.commit()

    except:
        traceback.print_exc()

    finally:
        session.close()


def main():

    # add_someone("John", 22)
    # get_someone("John")
    # add_someone("Mike", 28)
    # add_someone("Paul", 38)
    # update_someone("Mike", 30)
    get_everybody()
    # delete_someone("Paul")

    return


if __name__ == "__main__":
    main()