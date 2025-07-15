from getpass import getpass
from pathlib import Path

from moviedb import MovieDB, UserInfo


def handle_login_or_signup(db):
    user_id = None
    while not user_id:
        print("1. Login\n2. Signup")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            email = input("Email: ")
            password = getpass("Password: ")
            user_id = db.login(email, password)
            print("✅ Login successful!\n" if user_id else "❌ Invalid credentials.\n")
        elif choice == "2":
            user = UserInfo(
                fname=input("First name: "),
                lname=input("Last name: "),
                email=input("Email: "),
                password=getpass("Password: "),
                bio=input("Bio: "),
            )
            db.signup(user)
            print("✅ Signup successful. Please login.\n")
    return user_id


def show_menu():
    print("""
    ────────────────
    1. Add Movie (with Genre and Actors)
    2. Add Genre to Existing Movie
    3. Add Actor
    4. Link Actor to Existing Movie
    5. Review Movie
    6. Toggle Watchlist
    7. Add Friend
    8. Top 5 Movies
    9. Search Movie
    0. Logout
    ────────────────
    """)


def handle_add_movie_with_genres_actors(db):
    name = input("Movie name: ")
    desc = input("Description: ")
    date = input("Release date (YYYY-MM-DD): ")
    director = input("Director: ")
    db.add_movie(name, desc, date, director)

    while True:
        genre = input("Add genre (or leave blank to finish genres): ").strip()
        if not genre:
            break
        db.add_genre(name, genre)

    while True:
        actor_name = input("Add actor name (or leave blank to finish actors): ").strip()
        if not actor_name:
            break
        db.cur.execute("SELECT actor_id FROM actor WHERE name=?", (actor_name,))
        if not db.cur.fetchone():
            dob = input(f"DOB for {actor_name} (YYYY-MM-DD): ")
            movies_count = int(input(f"Movies count for {actor_name}: "))
            db.add_actor(actor_name, dob, movies_count)
        db.link_actor_to_movie(name, actor_name)


def handle_add_genre_to_existing_movie(db):
    movie_name = input("Movie name: ")
    genre = input("Genre: ")
    db.add_genre(movie_name, genre)


def handle_add_actor(db):
    name = input("Actor name: ")
    dob = input("DOB (YYYY-MM-DD): ")
    movies_count = int(input("Movies count: "))
    db.add_actor(name, dob, movies_count)
    print("✅ Actor added.")


def handle_link_actor_to_movie(db):
    movie_name = input("Movie name: ")
    actor_name = input("Actor name: ")
    db.link_actor_to_movie(movie_name, actor_name)
    print(f"✅ Actor '{actor_name}' linked to '{movie_name}'.")


def handle_review_movie(db, user_id):
    movie_name = input("Movie name to review: ")
    rating = float(input("Your rating (0-10): "))
    review_text = input("Optional review: ")
    db.review_movie(user_id, movie_name, rating, review_text)


def handle_toggle_watchlist(db, user_id):
    movie_name = input("Movie name to toggle watchlist: ")
    db.toggle_watchlist(user_id, movie_name)


def handle_add_friend(db, user_id):
    friend_email = input("Friend's email: ")
    db.add_friend(user_id, friend_email)


def handle_menu_choice(db, user_id):
    choice = input("Enter your choice: ").strip()

    match choice:
        case "1":
            handle_add_movie_with_genres_actors(db)
        case "2":
            handle_add_genre_to_existing_movie(db)
        case "3":
            handle_add_actor(db)
        case "4":
            handle_link_actor_to_movie(db)
        case "5":
            handle_review_movie(db, user_id)
        case "6":
            handle_toggle_watchlist(db, user_id)
        case "7":
            handle_add_friend(db, user_id)
        case "8":
            db.show_top_movies()
        case "9":
            db.search_movie(input("Search by keyword: "))
        case "0":
            return False
        case _:
            print("❗ Invalid option. Try again.")
    return True


def main(*args):
    current_file = Path(__file__).resolve()
    current_dir = current_file.parent
    db = MovieDB(current_dir)

    print("🎬 Welcome to MovieDB!\n")

    user_id = handle_login_or_signup(db)

    while True:
        show_menu()
        if not handle_menu_choice(db, user_id):
            print("👋 Logging out.")
            db.close()
            break


if __name__ == "__main__":
    main()
