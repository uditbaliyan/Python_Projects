from sqlalchemy import create_engine, text
from pathlib import Path

# db path
current_dir = Path(__file__).parent.resolve()
sqlite_path = current_dir / "db" / "tutorial.db"
engine = create_engine(f"sqlite:///{sqlite_path}", echo=True)

conn = engine.connect()

conn.execute(
    text(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR, age INTEGER)"
    )
)
conn.execute(
    text("INSERT INTO users (name, age) VALUES (:name, :age)"),
    [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}],
)
conn.commit()


# session = Session(engine)

# session.execute(
#     text("INSERT INTO users (name, age) VALUES (:name, :age)"),
#     [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}],
# )

# conn.commit()
