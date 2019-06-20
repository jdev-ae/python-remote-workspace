from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import dataset_reader
from config import DATABASE_URI
from models import Base, Book

# echo=True for SQL logging in console
engine = create_engine(DATABASE_URI, echo=True)

"""
Technically, you could execute commands on the engine, but we really want to use a session. 
Session's allow you to form transactions with the database where you can add objects (rows) 
to the session and commit them when ready. If any errors occur, you rollback the session 
to its previous state and nothing is stored.
"""
Session = sessionmaker(bind=engine)


def create_db():
    # only creates the tables into public schema not the database
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


def recreate_db():
    drop_db()
    create_db()


def add_book(book):
    s = Session()
    s.add(book)
    s.commit()
    s.close()


def get_all_books():
    s = Session()
    books = s.query(Book).all()
    s.close()
    return books


def create_googleplayapps_data():
    s = Session()
    data = dataset_reader.get_googleplaystore_data()
    for r in data: s.add(r)
    s.commit()
    s.close()


def create_imdb_metadata():
    s = Session()
    data = dataset_reader.get_imdb_metadata()
    for r in data:
        try:
            s.add(r)
        except:
            pass
    s.commit()
    s.close()
