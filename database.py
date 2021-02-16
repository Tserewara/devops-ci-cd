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


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)


def create_tables():
    Base.metadata.create_all(engine)


def populate_db():
    from sqlalchemy.orm import sessionmaker

    session = sessionmaker(bind=engine)()

    customers = ['Tsere', 'Alvaro', "Cris"]

    for customer in customers:
        session.add(Customers(name=customer))

    session.commit()
