from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, create_tables

engine = create_engine('postgresql://user:pass@localhost:5432/db')

connection = engine.connect()
print("Подключение успешно!")
connection.close()


Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

# new_user = User(name='Alice', email='alice@example.com')
# new_user2 = User(name='Alice2', email='alice2@example.com')
# session.add(new_user)
# session.add(new_user2)
# session.commit()  # Сохраняем изменения
# session.close()


# users = session.query(User).all()
# users = session.query(User).with_entities(User.email).all()
# users = session.query(User).filter(User.name == "Alice").all()
users = session.query(User).filter(User.name == "Alice").order_by(User.name).all()

print(users)
for user in users:
    print(f"user: {user.name}, email: {user.email}")