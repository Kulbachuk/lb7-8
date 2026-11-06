import pytest
from unittest.mock import patch
from publishing.models import Author, Book, Tag, AuthorProfile

@pytest.mark.django_db
class TestDjangoPublishing:

    # 1. Перевірка __str__ методу книги
    def test_book_str(self, sample_book):
        assert str(sample_book) == "Рефакторинг (2026)"

    # 2. Значення за замовчуванням (is_available та published_year)
    def test_book_defaults(self, sample_book):
        assert sample_book.is_available is True
        assert sample_book.published_year == 2026

    # 3. Параметризований тест валідації ціни (Завдання 5)
    @pytest.mark.parametrize("price, valid", [
        (500.00, True),
        (0.00, True),
        (-10.00, False),
    ])
    def test_price_validation(self, sample_author, price, valid):
        book = Book(title="Test", price=price, description="Desc", author=sample_author)
        if not valid:
            with pytest.raises(Exception):
                book.full_clean()
                book.save()

    # 4. Перевірка унікальності Email автора
    def test_author_email_unique(self, sample_author):
        with pytest.raises(Exception):
            Author.objects.create(name="Дублікат", email=sample_author.email)

    # 5. Мок зовнішньої залежності/виклику (Завдання 7)
    @patch('publishing.models.Author.save')
    def test_author_save_mock(self, mock_save):
        author = Author(name="Mock Author", email="mock@test.com")
        author.save()
        assert mock_save.called