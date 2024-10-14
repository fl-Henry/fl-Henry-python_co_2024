from sqlalchemy import Column, Integer, String, create_engine, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Поле для уникального идентификатора
    name = Column(String(50))  # Поле для хранения имени пользователя
    email = Column(String)  # Поле для хранения электронной почты
    note = Column(Text, default='Default note')


def create_tables(engine):
    Base.metadata.create_all(engine)

