from datetime import datetime

import crud
from models import Book

crud.create_db()

book = Book(
    title='Deep Learning',
    author='Ian Goodfellow',
    pages=775,
    published=datetime(2016, 11, 18)
)

# crud.add_book(book)
# books = crud.get_all_books()
# for book in books:
#     print(book)


# crud.create_googleplayapps_data()
crud.create_imdb_metadata()