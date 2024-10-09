from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Поле для уникального идентификатора
    name = Column(String)  # Поле для хранения имени пользователя
    email = Column(String)  # Поле для хранения электронной почты


def create_tables(engine):
    Base.metadata.create_all(engine)
