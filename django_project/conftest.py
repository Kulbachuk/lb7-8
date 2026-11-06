import pytest
from publishing.models import Author, Book

@pytest.fixture
def sample_author(db):
    return Author.objects.create(name="Мартин Фаулер", email="fowler@refactoring.com")

@pytest.fixture
def sample_book(db, sample_author):
    return Book.objects.create(
        title="Рефакторинг",
        price=950.00,
        description="Покращення дизайну існуючого коду",
        author=sample_author
    )