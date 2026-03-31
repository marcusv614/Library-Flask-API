from flask import Flask, request, jsonify
from db import db
from flask_migrate import Migrate 
from models.book import Book

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

@app.route("/books",methods=['POST'])
def add_book():
    data = request.get_json(silent=True)
    if not data or not all(key in data for key in ('title', 'author', 'description')):
        return jsonify({
            'error': 'Envie JSON válido com title, author e description.'
        }), 400

    newbook = Book(
        title=data['title'],
        author=data['author'],
        description=data['description']
    )
    db.session.add(newbook)
    db.session.commit()
    return jsonify({'message': 'Livro inserido com sucesso'}), 201

@app.route("/books", methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.as_dict() for book in books]), 200

@app.route('/books/<uuid:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Livro não encontrado'}), 404
    return jsonify(book.as_dict()), 200

@app.route('/books/<uuid:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Livro não encontrado'}), 404

    data = request.get_json(silent=True)
    if not data or not any(key in data for key in ('title', 'author', 'description', 'isFavorite', 'isReading', 'isFinished')):
        return jsonify({'error': 'Envie JSON válido com pelo menos um campo para atualizar.'}), 400

    if 'title' in data:
        book.title = data['title']
    if 'author' in data:
        book.author = data['author']
    if 'description' in data:
        book.description = data['description']
    if 'isFavorite' in data:
        book.isFavorite = bool(data['isFavorite'])
    if 'isReading' in data:
        book.isReading = bool(data['isReading'])
    if 'isFinished' in data:
        book.isFinished = bool(data['isFinished'])

    db.session.commit()
    return jsonify({'message': 'Livro atualizado com sucesso', 'book': book.as_dict()}), 200

@app.route('/books/<uuid:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Livro não encontrado'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Livro removido com sucesso'}), 200

if __name__ == "__main__":
    app.run(debug=True,port=8080,host="0.0.0.0")