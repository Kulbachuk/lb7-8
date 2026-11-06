from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate
from models import db, Author, Book, Tag, AuthorProfile

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask-super-secret-key-12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    books = Book.query.all()
    return f"Каталог Flask (Всього книг у БД: {len(books)})"

if __name__ == '__main__':
    app.run(debug=True, port=5001)