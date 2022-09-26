import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'HW10.db')
