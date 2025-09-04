import csv
import re
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set


class Patron:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.id = uuid.uuid4()
        self.age = age
        self.books_read: Set[str] = set()  # ISBNs
        self.books_borrowed: Dict[str, datetime] = {}  # ISBN -> due_date

    def borrow_book(self, book: "Book") -> None:
        self.books_borrowed[book.isbn] = book.due_date

    def return_book(self, isbn: str) -> None:
        self.books_read.add(isbn)
        self.books_borrowed.pop(isbn, None)

    def __repr__(self) -> str:
        return f"Patron({self.name}, {self.age} yrs, ID: {self.id})"


class Book:
    def __init__(
        self, title: str, author: str, isbn: str, year: int, availability: bool = True
    ) -> None:
        self._title = title
        self._author = author
        self._isbn = isbn
        self._year = year
        self._availability = availability
        self._due_date: Optional[datetime] = None

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        self._author = value

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("ISBN must be a string.")
        self._isbn = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        self._year = value

    @property
    def availability(self) -> bool:
        return self._availability

    @availability.setter
    def availability(self, value: bool) -> None:
        self._availability = value

    @property
    def due_date(self) -> Optional[datetime]:
        return self._due_date

    @due_date.setter
    def due_date(self, value: Optional[datetime]) -> None:
        self._due_date = value

    def __repr__(self) -> str:
        status = (
            "Available"
            if self.availability
            else f"Due by {self.due_date.strftime("%Y-%m-%d")}"
        )
        return f"{self.title} by {self.author} ({self.year}) - ISBN: {self.isbn} | {status}"


class Library:
    BORROW_PERIOD_DAYS = 14
    FINE_PER_DAY = 1.0

    def __init__(self) -> None:
        self.catalog: Dict[str, Book] = {}  # ISBN -> Book
        self.patrons: Dict[uuid.UUID, Patron] = {}

    def add_book(self, book: Book) -> None:
        if book.isbn in self.catalog:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self.catalog[book.isbn] = book

    def register_patron(self, patron: Patron) -> None:
        if patron.id in self.patrons:
            raise ValueError("Patron already registered.")
        self.patrons[patron.id] = patron

    def search(self, pattern: str) -> List[Book]:
        regex = re.compile(pattern, re.IGNORECASE)
        return [
            book
            for book in self.catalog.values()
            if regex.search(book.title) or regex.search(book.author)
        ]

    def borrow_book(self, isbn: str, patron_id: uuid.UUID) -> None:
        if patron_id not in self.patrons:
            raise ValueError("Patron not registered.")

        book = self.catalog.get(isbn)
        patron = self.patrons[patron_id]

        if not book:
            raise ValueError("Book not found.")
        if not book.availability:
            raise ValueError("Book is currently borrowed.")

        due_date = datetime.now() + timedelta(days=self.BORROW_PERIOD_DAYS)
        book.availability = False
        book.due_date = due_date

        patron.borrow_book(book)

    def return_book(self, isbn: str, patron_id: uuid.UUID) -> float:
        if patron_id not in self.patrons:
            raise ValueError("Patron not registered.")

        book = self.catalog.get(isbn)
        patron = self.patrons[patron_id]

        if not book or book.availability:
            raise ValueError("Book is not borrowed.")

        now = datetime.now()
        fine = 0.0
        if book.due_date and now > book.due_date:
            overdue_days = (now - book.due_date).days
            fine = overdue_days * self.FINE_PER_DAY

        book.availability = True
        book.due_date = None

        patron.return_book(isbn)

        return fine

    def available_books(self) -> List[Book]:
        return [book for book in self.catalog.values() if book.availability]

    def export_catalog(self, filename: str) -> None:
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "Title",
                "Author",
                "ISBN",
                "Year",
                "Availability",
                "Due Date",
            ])
            for book in self.catalog.values():
                writer.writerow([
                    book.title,
                    book.author,
                    book.isbn,
                    book.year,
                    "Yes" if book.availability else "No",
                    book.due_date.strftime("%Y-%m-%d") if book.due_date else "",
                ])

    @property
    def total_books(self) -> int:
        return len(self.catalog)


def main():
    lib = Library()

    # Books
    b1 = Book("1984", "George Orwell", "12345", 1949)
    b2 = Book("Brave New World", "Aldous Huxley", "67890", 1932)
    lib.add_book(b1)
    lib.add_book(b2)

    # Patron
    patron = Patron("Alice", 30)
    lib.register_patron(patron)

    print("Search results for 'Orwell':", lib.search("Orwell"))

    # Borrow and return
    lib.borrow_book("12345", patron.id)
    print(lib.catalog["12345"])

    fine = lib.return_book("12345", patron.id)
    print(f"Fine: ${fine:.2f}")

    # Export catalog
    # lib.export_catalog("catalog.csv")


if __name__ == "__main__":
    main()
