# from sqlalchemy import Column, Integer, String, create_engine, Text
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = 'users'  # Имя таблицы в базе данных
#
#     id = Column(Integer, primary_key=True)  # Поле для уникального идентификатора
#     name = Column(String(50), unique=True)  # Поле для хранения имени пользователя
#     email = Column(String)  # Поле для хранения электронной почты
#     note = Column(Text, default='Default note')
#
#
def create_tables(engine):
    Base.metadata.create_all(engine)


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     profile = relationship("UserProfile", back_populates="user", uselist=False)
#
#
# class UserProfile(Base):
#     __tablename__ = 'user_profiles'
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     bio = Column(String)
#
#     user = relationship("User", back_populates="profile")

from sqlalchemy import Table

enrollment = Table('enrollment', Base.metadata,
                   Column('student_id', Integer, ForeignKey('students.id')),
                   Column('course_id', Integer, ForeignKey('courses.id'))
                   )


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship("Course", secondary=enrollment, back_populates="students")


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship("Student", secondary=enrollment, back_populates="courses")