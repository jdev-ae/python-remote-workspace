from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

# We need to inherit Base in order to register models with SQA. Without this, SQA wouldn't know anything about our models.
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)

    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>" \
            .format(self.title, self.author, self.pages, self.published)


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('parent.id'))


class GooglePlayApp(Base):
    __tablename__ = 'googleplayapps'
    id = Column(Integer, primary_key=True)
    app_name = Column(String, nullable=False)
    category = Column(String)
    app_rating = Column(Float)
    reviews = Column(Integer)
    size = Column(String)
    installs = Column(String)
    app_type = Column(String)
    price = Column(String)
    content_rating = Column(String)
    genres = Column(String)
    last_updated = Column(DateTime)
    current_ver = Column(String)
    android_ver = Column(String)

    def __repr__(self):
        return "id = '{}', app_name = '{}', category = '{}', app_rating = '{}', reviews = '{}', size = '{}', installs = '{}', app_type = '{}', " \
               "price = '{}', content_rating = '{}', genres = '{}', last_updated = '{}', current_ver = '{}', android_ver = '{}'".format(
            self.id, self.app_name, self.category, self.app_rating, self.reviews, self.size, self.installs, self.app_type, self.price, self.content_rating,
            self.genres, self.last_updated, self.current_ver, self.android_ver)


class IMDBMovie(Base):
    __tablename__ = 'IMDBMovies'
    id = Column(Integer, primary_key=True)
    movie_title = Column(String, nullable=False)
    director_name = Column(String, nullable=False)
    color = Column(Boolean)
    duration = Column(Float, default=0)
    actor_1_name = Column(String)
    language = Column(String)
    country = Column(String)
    title_year = Column(Integer)

    def __repr__(self):
        return "id = '{}', movie_title = '{}', director_name = '{}', color = '{}', duration = '{}', actor_1_name = '{}', " \
               "language = '{}', country = '{}', title_year = '{}'".format(self.id, self.movie_title, self.director_name, self.color,
                                                                           self.duration, self.actor_1_name, self.language, self.country, self.title_year, )
