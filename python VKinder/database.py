import sqlalchemy
from sqlalchemy.orm import declarative_base


Base = declarative_base()
engine = sqlalchemy.create_engine(Base)
connection = engine.connect()


# создать таблицу с пользователями в БД
connection.execute("""
                    create table if not exists Users (
                    request_user_id integer not null, 
                    matched_user_id integer not null, 
                    screen_name varchar(20), 
                    constraint pk primary key (request_user_id, matched_user_id)
                    );""")


# создать таблицу с полями пользователя в БД
connection.execute("""
                    create table if not exists Fields (
                    request_user_id integer unique not null,
                    age integer, 
                    sex varchar(20), 
                    city integer
                    );""")


# добавление нового пользователя
def insert_users(request_user_id, matched_user_id, screen_name):
    connection.execute("""
                        insert into Users(
                        request_user_id
                        matched_user_id
                        screen_name)
                        values (%s, %s, %s);
                        """, (request_user_id, matched_user_id, screen_name))


# создание строки для пользователя
def insert_friends(request_user_id):
    connection.execute("""
                        insert into file (request_user_id) values (%s);
                        """, request_user_id)


def update_age(request_user_id, age):
    connection.execute("""
                        update files set age = (%s) where request_user_id = (%s);
                        """, (age, request_user_id))


def update_sex(request_user_id, sex):
    connection.execute("""
                        update files set sex = (%s) where request_user_id = (%s);
                        """, (sex, request_user_id))


def update_city(request_user_id, city):
    connection.execute("""
                        update files set city = (%s) where request_user_id = (%s);
                        """, (city, request_user_id))


def select(request_user_id):
    files = connection.execute("""
                            select 
                            age,
                            sex,
                            city
                            from files where request_user_id = (%s);
                            """, request_user_id).fetchone()
    return files


def insert_fields(request_user_id):
    return None