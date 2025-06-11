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
    'title',
    
)