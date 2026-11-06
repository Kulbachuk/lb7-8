from app import app
from models import db, Author, AuthorProfile, Book, Tag

def run_flask_demo():
    with app.app_context():
        print("--- 1. Перевірка транзакційності Unit of Work ---")
        try:
            author = Author(name="Роберт Мартін", email="unclebob@example.com")
            db.session.add(author)
            db.session.flush()  # Отримуємо ID автора у межах тієї ж транзакції

            profile = AuthorProfile(author_id=author.id, bio="Експерт з чистого коду", rating=4.9)
            tag = Tag(name="Clean Code")
            book = Book(title="Чистий код", price=850.0, description="Професійна розробка ПЗ", author_id=author.id)
            book.tags.append(tag)

            db.session.add_all([profile, tag, book])
            db.session.commit()  # Атомарна фіксація
            print("Успішно збережено об'єкти у Flask БД!")
        except Exception as e:
            db.session.rollback()  # Відкат у разі помилки
            print(f"Помилка транзакції, виконано rollback: {e}")

        print("\n--- 2. Перевірка вибірки даних через ORM ---")
        books = Book.query.all()
        for b in books:
            print(f"Flask Book: '{b.title}' | Автор: {b.author.name}")

if __name__ == '__main__':
    run_flask_demo()