import os
import sys
import django

# Обов'язково додаємо папку django_project у шляхи Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from publishing.models import Author, AuthorProfile, Book, Tag
from django.db.models import Q, Avg

def run():
    author, _ = Author.objects.get_or_create(name="Мартин Фаулер", email="fowler@refactoring.com")
    AuthorProfile.objects.get_or_create(author=author, bio="Експерт з архітектури", rating=4.9)
    tag, _ = Tag.objects.get_or_create(name="Architecture", slug="arch")

    book, _ = Book.objects.get_or_create(
        title="Рефакторинг",
        price=900.00,
        description="Покращення коду",
        author=author
    )
    book.tags.add(tag)

    q_books = Book.objects.filter(Q(price__gte=500) | Q(published_year=2026))
    print(f"Знайдено книг за умовою Q: {q_books.count()}")

    print("Середня ціна книг:", Book.objects.aggregate(Avg('price')))
    
    opt_books = Book.objects.select_related('author', 'author__profile').prefetch_related('tags').all()
    for b in opt_books:
        print(f"Книга: {b.title} | Автор: {b.author.name} (Рейтинг: {b.author.profile.rating})")

if __name__ == '__main__':
    run()