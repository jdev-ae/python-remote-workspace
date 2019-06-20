_user = 'surendra'
_password = 'password'
_host = 'localhost'
_port = 5432
_database = 'sqlalchemy_test'

DATABASE_URI = 'postgres+psycopg2://{}:{}@{}:{}/{}'
DATABASE_URI = DATABASE_URI.format(_user, _password, _host, _port, _database)
