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
    data = request.get_json()
    newbook = Book(title=data['title'],author=data['author'],description=data['description']) # type: ignore
    db.session.add(newbook)
    db.session.commit()
    return jsonify({'message: livro inserido com sucesso' }), 201

if __name__ == "__main__":
    app.run(debug=True,port=8080,host="0.0.0.0")