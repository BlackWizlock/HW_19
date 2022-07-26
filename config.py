class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PWD_HASH_SALT = b'bI@FaTS3cR3T'
    PWD_HASH_ITERATIONS = 100_000
    SECRET_HERE = '249y823r9v8238r9u'
    ALGORITH = 'HS256'
    RESTX_JSON = {'ensure_ascii': False}
    JSON_AS_ASCII = False
