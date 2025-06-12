import pytest
from book import Book

@pytest.mark.parametrize(
    'title, isbn',
    [
        ('Watchmen', '978-1779501127'),
        ('1984', '9780451524935'),
        ('Python Programming', '978-0135166307')
    ]
)

def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn

@pytest.mark.parametrize(
    'title', [
        "",
])

def test_creation_with_invalid_title(title):
    with pytest.raises(RuntimeError):
        Book(title, "987-1779501127")

@pytest.mark.parametrize("isbn", [
    "978-1779501128",      # incorrect checksum
    "978-177950112",       # only 12 digits
    "978-17795011278",     # 14 digits
    "978-17795011A7",      # contains letter
    "",                    # empty string
])

def test_with_invalid_isbn(isbn):
    with pytest.raises(RuntimeError):
        Book("Valid Title", isbn)