from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return "Hello!"

@app.route('/books')
def get_books():
    books = Book.query.all()
    return [{
        "id": b.id,
        "title": b.book_name,
        "author": b.author,
        "publisher": b.publisher
    } for b in books]

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return{
        "id": book.id,
        "title": book.book_name,
        "author": book.author,
        "publisher": book.publisher
    }

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['title'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {
        "id": book.id,
        "title": book.book_name,
        "author": book.author,
        "publisher": book.publisher
    }

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return f"Book with id {id} has been deleted."