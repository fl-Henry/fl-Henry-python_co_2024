from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import create_tables, Student, Course

engine = create_engine('postgresql://user:pass@localhost:5432/db')

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

# new_user = User(name='Alice')
# # new_user2 = User(name='Alice')
# session.add(new_user)
# # session.add(new_user2)
# session.commit()
# session.close()