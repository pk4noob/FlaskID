from settings.settings import BasteSettings
import os


class DevelopSettings(BasteSettings):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  "postgres://postgres:test123@127.0.0.1:5432/MoviesDB"