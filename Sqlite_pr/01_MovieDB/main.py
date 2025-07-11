import sqlite3
from pathlib import Path

class MovieDB:
    """"""
    def __init__(self, db_file):
        """"""
        self.conn = sqlite3.connect(db_file/"MovieDB.db")
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """"""
        # create table
        pass

    def add_movie(self, title, year, score):
        """"""
        # insert movie
        pass

    def get_all_movies(self):
        """"""
        # fetch and return list
        pass

    def close(self):
        """"""
        self.conn.close()


def main(*args):
    """Docstring"""
    current_file = Path(__file__).resolve()
    current_dir = current_file.parent
    pass
if __name__ == '__main__':
    main()