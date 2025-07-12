from pathlib import Path
from getpass import getpass
from moviedb import MovieDB

def main(*args):
    current_file = Path(__file__).resolve()
    current_dir = current_file.parent
    db = MovieDB(current_dir)

    print("🎬 Welcome to MovieDB!\n")
    user_id = None

    while not user_id:
        print("1. Login\n2. Signup")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            email = input("Email: ")
            password = getpass("Password: ")
            user_id = db.login(email, password)
            if user_id:
                print("✅ Login successful!\n")
            else:
                print("❌ Invalid credentials.\n")

        elif choice == '2':
            fname = input("First name: ")
            lname = input("Last name: ")
            email = input("Email: ")
            password = getpass("Password: ")
            bio = input("Bio: ")
            db.signup(fname, lname, email, password, bio)
            print("✅ Signup successful. Please login.\n")

    while True:
        print("""
        ────────────────
        1. Add Movie
        2. Add Genre to Movie
        3. Add Actor
        4. Link Actor to Movie
        5. Review Movie
        6. Toggle Watchlist
        7. Add Friend
        8. Top 5 Movies
        9. Search Movie
        0. Logout
        ────────────────
        """)
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Movie name: ")
            desc = input("Description: ")
            date = input("Release date (YYYY-MM-DD): ")
            director = input("Director: ")
            db.add_movie(name, desc, date, director)

        elif choice == '2':
            movie_name = input("Movie name: ")
            genre = input("Genre: ")
            db.add_genre(movie_name, genre)
            print("Genre added.")

        elif choice == '3':
            name = input("Actor name: ")
            dob = input("DOB (YYYY-MM-DD): ")
            movies_count = int(input("Movies count: "))
            db.add_actor(name, dob, movies_count)
            print("Actor added.")

        elif choice == '4':
            movie_name = input("Movie name: ")
            actor_name = input("Actor name: ")
            db.link_actor_to_movie(movie_name, actor_name)
            print("Actor linked to movie.")

        elif choice == '5':
            movie_name = input("Movie name to review: ")
            rating = float(input("Your rating (0-10): "))
            review_text = input("Optional review: ")
            db.review_movie(user_id, movie_name, rating, review_text)

        elif choice == '6':
            movie_name = input("Movie name to add/remove from watchlist: ")
            db.toggle_watchlist(user_id, movie_name)

        elif choice == '7':
            friend_email = input("Friend's email: ")
            db.add_friend(user_id, friend_email)

        elif choice == '8':
            print("Top 5 Movies:")
            db.show_top_movies()

        elif choice == '9':
            keyword = input("Search by keyword: ")
            db.search_movie(keyword)

        elif choice == '0':
            print("👋 Logging out.")
            db.close()
            break

        else:
            print("❗ Invalid option. Try again.")

if __name__ == '__main__':
    main()
