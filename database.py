import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


def get_postgres_uri():
    host = os.environ.get('POSTGRES_HOST')
    port = 5432
    password = os.environ.get('POSTGRES_PASSWORD')
    user, db_name = 'postgres', 'damarowahutu'
    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'


engine = create_engine(get_postgres_uri())

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    tag = Column(String)


def create_tables():
    Base.metadata.create_all(engine)


def populate_db():
    from sqlalchemy.orm import sessionmaker

    session = sessionmaker(bind=engine)()

    posts = [
        {
            "title": "First Post",
            "description": "A very useful post",
            "tag": "tip"
        },
        {
            "title": "Second Post",
            "description": "A very useful post",
            "tag": "guide"
        },
        {
            "title": "Third Post",
            "description": "A very useful post",
            "tag": "tip"
        },
    ]

    for post in posts:
        session.add(
            Post(title=post['title'],
                 description=post['description'],
                 tag=post['tag']
                 )
        )

    session.commit()
