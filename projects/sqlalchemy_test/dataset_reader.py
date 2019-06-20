import csv
from datetime import datetime

from models import GooglePlayApp, IMDBMovie


def get_googleplaystore_data():
    rv = []
    with open('/Users/surendra/Desktop/google-play-store-apps/googleplaystore.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', )
        next(data, None)
        for row in data:
            app = GooglePlayApp()
            row[-3] = datetime.strptime(row[-3], '%B %d, %Y')
            try:
                app.app_name, app.category, app.app_rating, app.reviews, app.size, app.installs, app.app_type, \
                app.price, app.content_rating, app.genres, app.last_updated, app.current_ver, app.android_ver = row
                rv.append(app)
            except:
                pass
    return rv


def get_imdb_metadata():
    rv = []
    with open('/Users/surendra/Desktop/movie_metadata.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', )
        next(data, None)
        for row in data:
            movie = IMDBMovie()
            row[2] = row[2].lower() == 'color'
            try:
                movie.movie_title, movie.director_name, movie.color, movie.duration, movie.actor_1_name, movie.language, movie.country, movie.title_year = row
                rv.append(movie)
            except:
                pass
    return rv
