import pytest
from unittest.mock import patch
from models import Book, Author

def test_flask_models(app):
    with app.app_context():
        author = Author(name="Дональд Кнут", email="knuth@stanford.edu")
        book = Book(title="Мистецтво програмування", price=1200.0, description="Том 1", author=author)
        assert repr(book) == '<Book Мистецтво програмування>'

def test_home_page_flask(client):
    res = client.get('/')
    assert res.status_code == 200
    assert "Каталог Flask" in res.data.decode('utf-8')

@patch('models.Book.query')
def test_mock_book_query(mock_query, client):
    mock_query.all.return_value = []
    res = client.get('/')
    assert res.status_code == 200