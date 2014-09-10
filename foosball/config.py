class Config(object):
    DEBUG = True
    DATABASE = 'foosball.db'
    # DATABASE_URI = 'sqlite://
    LOG_FILE = '/var/log/foosball/foosball.log'

class DebugConfig(Config):
    LOG_FILE = 'foosball.log'
