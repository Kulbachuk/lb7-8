from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Проміжна таблиця Many-to-Many
book_tags = db.Table('book_tags',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    books = db.relationship('Book', backref='author', lazy=True, cascade="all, delete-orphan")
    profile = db.relationship('AuthorProfile', backref='author', uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Author {self.name}>'


class AuthorProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False, unique=True)
    bio = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, default=5.0)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    
    tags = db.relationship('Tag', secondary=book_tags, backref=db.backref('books', lazy='dynamic'))

    def __repr__(self):
        return f'<Book {self.title}>'