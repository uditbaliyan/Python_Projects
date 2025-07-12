import sqlite3
from pathlib import Path


def create_connection(db_file):
    """Create a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"[Error] Connection failed: {e}")
        return None


def create_table(cursor):
    """Create movie table if it doesn't exist."""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movie (
                title TEXT,
                year INTEGER,
                score REAL
            )
        """)
    except sqlite3.Error as e:
        print(f"[Error] Failed to create table: {e}")


def insert_data(cursor):
    """Insert movie data safely using parameters."""
    try:
        movies = [
            ("Monty Python and the Holy Grail", 1975, 8.2),
            ("And Now for Something Completely Different", 1971, 7.5),
        ]
        cursor.executemany(
            "INSERT INTO movie (title, year, score) VALUES (?, ?, ?)", movies
        )
    except sqlite3.Error as e:
        print(f"[Error] Failed to insert data: {e}")


def fetch_data(cursor):
    """Fetch and print all movie records."""
    try:
        cursor.execute("SELECT * FROM movie")
        rows = cursor.fetchall()
        print("Movies in database:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"[Error] Failed to fetch data: {e}")


def main():
    # Absolute path to the current script
    current_file = Path(__file__).resolve()
    current_dir = current_file.parent
    conn = create_connection(current_dir / "tutorial.db")
    if conn is None:
        return

    try:
        cur = conn.cursor()
        create_table(cur)
        insert_data(cur)
        conn.commit()
        fetch_data(cur)
    except Exception as e:
        print(f"[Unhandled Error] {e}")
    finally:
        conn.close()
        print("📦 Connection closed.")


if __name__ == "__main__":
    print(f"variable = {__name__}")
    main()
