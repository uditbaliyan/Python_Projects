import sqlite3
from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserInfo:
    fname: str
    lname: str
    email: str
    password: str
    bio: str


class MovieDB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path / "MovieDB.db")
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.executescript("""
            BEGIN;
            CREATE TABLE IF NOT EXISTS user (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT UNIQUE,
                password TEXT,
                bio TEXT,
                creation_date TEXT,
                last_login TEXT
            );

            CREATE TABLE IF NOT EXISTS login_history (
                history_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                login_time TEXT,
                FOREIGN KEY(user_id) REFERENCES user(user_id)
            );

            CREATE TABLE IF NOT EXISTS movie (
                movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                release_date TEXT,
                director TEXT,
                rating REAL DEFAULT 0.0
            );

            CREATE TABLE IF NOT EXISTS genre (
                genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER,
                genre TEXT,
                FOREIGN KEY(movie_id) REFERENCES movie(movie_id)
            );

            CREATE TABLE IF NOT EXISTS actor (
                actor_id INTEGER PRIMARY KEY,
                name TEXT,
                dob TEXT,
                movies_count INTEGER
            );

            CREATE TABLE IF NOT EXISTS movie_actor (
                movie_id INTEGER,
                actor_id INTEGER,
                FOREIGN KEY(movie_id) REFERENCES movie(movie_id),
                FOREIGN KEY(actor_id) REFERENCES actor(actor_id),
                PRIMARY KEY (movie_id, actor_id)
            );

            CREATE TABLE IF NOT EXISTS collection (
                user_id INTEGER,
                movie_id INTEGER,
                rating REAL,
                watchlist BOOLEAN DEFAULT FALSE,
                review TEXT,
                PRIMARY KEY (user_id, movie_id),
                FOREIGN KEY(user_id) REFERENCES user(user_id),
                FOREIGN KEY(movie_id) REFERENCES movie(movie_id)
            );

            CREATE TABLE IF NOT EXISTS friendlist (
                user_id INTEGER,
                friend_id INTEGER,
                PRIMARY KEY (user_id, friend_id),
                FOREIGN KEY(user_id) REFERENCES user(user_id),
                FOREIGN KEY(friend_id) REFERENCES user(user_id)
            );
            COMMIT;
        """)

    def signup(self, user: UserInfo):
        self.cur.execute(
            """
            INSERT INTO user (first_name, last_name, email, password, bio, creation_date, last_login)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user.fname,
                user.lname,
                user.email,
                user.password,
                user.bio,
                datetime.now(),
                datetime.now(),
            ),
        )
        self.conn.commit()

    def login(self, email, password):
        self.cur.execute(
            "SELECT user_id FROM user WHERE email=? AND password=?", (email, password)
        )
        user = self.cur.fetchone()
        if user:
            now = datetime.now()
            self.cur.execute(
                "UPDATE user SET last_login=? WHERE user_id=?", (now, user[0])
            )
            self.cur.execute(
                "INSERT INTO login_history (user_id, login_time) VALUES (?, ?)",
                (user[0], now),
            )
            self.conn.commit()
            return user[0]
        return None

    def add_movie(self, name, desc, date, director):
        self.cur.execute(
            """
            INSERT INTO movie (name, description, release_date, director)
            VALUES (?, ?, ?, ?)
        """,
            (name, desc, date, director),
        )
        self.conn.commit()
        print("Movie added successfully.\n")

    def add_genre(self, movie_name, genre):
        self.cur.execute("SELECT movie_id FROM movie WHERE name=?", (movie_name,))
        movie = self.cur.fetchone()
        if movie:
            self.cur.execute(
                "INSERT INTO genre (movie_id, genre) VALUES (?, ?)", (movie[0], genre)
            )
            self.conn.commit()

    def add_actor(self, name, dob, movies_count):
        self.cur.execute(
            "INSERT INTO actor (name, dob, movies_count) VALUES (?, ?, ?)",
            (name, dob, movies_count),
        )
        self.conn.commit()

    def link_actor_to_movie(self, movie_name, actor_name):
        self.cur.execute("SELECT movie_id FROM movie WHERE name=?", (movie_name,))
        movie = self.cur.fetchone()
        self.cur.execute("SELECT actor_id FROM actor WHERE name=?", (actor_name,))
        actor = self.cur.fetchone()
        if movie and actor:
            self.cur.execute(
                "INSERT OR IGNORE INTO movie_actor (movie_id, actor_id) VALUES (?, ?)",
                (movie[0], actor[0]),
            )
            self.conn.commit()

    def review_movie(self, user_id, movie_name, rating, review_text=""):
        self.cur.execute("SELECT movie_id FROM movie WHERE name=?", (movie_name,))
        row = self.cur.fetchone()
        if not row:
            print("Movie not found.")
            return
        movie_id = row[0]

        self.cur.execute(
            """
            INSERT OR REPLACE INTO collection (user_id, movie_id, rating, review)
            VALUES (?, ?, ?, ?)
        """,
            (user_id, movie_id, rating, review_text),
        )

        self.cur.execute(
            "SELECT AVG(rating) FROM collection WHERE movie_id=?", (movie_id,)
        )
        avg_rating = self.cur.fetchone()[0]
        self.cur.execute(
            "UPDATE movie SET rating=? WHERE movie_id=?", (avg_rating, movie_id)
        )
        self.conn.commit()
        print("Review added.\n")

    def toggle_watchlist(self, user_id, movie_name):
        self.cur.execute("SELECT movie_id FROM movie WHERE name=?", (movie_name,))
        row = self.cur.fetchone()
        if row:
            movie_id = row[0]
            self.cur.execute(
                "SELECT watchlist FROM collection WHERE user_id=? AND movie_id=?",
                (user_id, movie_id),
            )
            entry = self.cur.fetchone()
            if entry:
                new_val = not entry[0]
                self.cur.execute(
                    "UPDATE collection SET watchlist=? WHERE user_id=? AND movie_id=?",
                    (new_val, user_id, movie_id),
                )
            else:
                self.cur.execute(
                    "INSERT INTO collection (user_id, movie_id, watchlist) VALUES (?, ?, ?) ",
                    (user_id, movie_id, True),
                )
            self.conn.commit()
            print("Watchlist updated.\n")

    def add_friend(self, user_id, friend_email):
        self.cur.execute("SELECT user_id FROM user WHERE email=?", (friend_email,))
        row = self.cur.fetchone()
        if row:
            friend_id = row[0]
            self.cur.execute(
                "INSERT OR IGNORE INTO friendlist (user_id, friend_id) VALUES (?, ?)",
                (user_id, friend_id),
            )
            self.conn.commit()
            print("Friend added.\n")
        else:
            print("User not found.\n")

    def show_top_movies(self):
        self.cur.execute("""
            SELECT name, rating FROM movie
            ORDER BY rating DESC
            LIMIT 5
        """)
        for name, rating in self.cur.fetchall():
            print(f"{name} - {rating}/10")

    def search_movie(self, keyword):
        self.cur.execute(
            """
            SELECT name, description, rating FROM movie
            WHERE name LIKE ? OR description LIKE ?
        """,
            (f"%{keyword}%", f"%{keyword}%"),
        )
        results = self.cur.fetchall()
        if results:
            for name, desc, rating in results:
                print(f"{name} ({rating}/10)\n  {desc}\n")
        else:
            print("No movies found.")

    def close(self):
        self.conn.close()
