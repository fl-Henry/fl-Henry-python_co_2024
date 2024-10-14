from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import sessionmaker

from models import create_tables, User

engine = create_engine('postgresql://user:pass@localhost:5432/db')

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

# Создаем нового пользователя
new_user = User(id='15s', name='John Doe', email='john@example.com')
# Добавляем пользователя в сессию
session.add(new_user)
# Сохраняем изменения в базе данных
session.commit()


# new_users = [
#     User(name='Alice', email='alice@example.com'),
#     User(name='Bob', email='bob@example.com'),
#     User(name='Charlie', email='charlie@example.com')
# ]
# session.add_all(new_users)
#
# # session.add(User(name='Alice', email='alice@example.com'),)
# # session.add(User(name='Bob', email='bob@example.com'),)
# # session.add(User(name='Charlie', email='charlie@example.com'))
#
# session.commit()


# users = session.query(User).filter_by(note='Default note').all()
# print("users:", users)
#
# if users:
#     for user, index in zip(users, range(len(users))):
#         user.note = f'Changed note {index}'
#         session.commit()


# # Массовое обновление всех пользователей с определенным доменом
# session.query(User) \
#     .filter(User.email.like('%@example.com')) \
#     .update({"email": "updated@example.com"}, synchronize_session=False)
#
# session.commit()