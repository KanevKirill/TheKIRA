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


