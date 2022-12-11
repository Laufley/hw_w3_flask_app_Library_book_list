from app import app
from flask import render_template, request, redirect
from models.collection import collection_of_books, favourites_collection
from models.book import Book

@app.route('/home')
def index():
    return render_template('index.html', title="Books for Ducks", shelves= collection_of_books)

@app.route('/home', methods = ['POST'])
def add_book():
    title = request.form["title_new_book"]
    author = request.form["author_new_book"]
    genre = request.form["genre_new_book"]
    available = True
    new_book = Book(title, author, genre, available)
    collection_of_books.append(new_book)
    return redirect('/home')

@app.route('/home/favourites/<book_ID>', methods = ['POST'])
def move_to_favs(book_ID):
    book = collection_of_books[int(book_ID)]
    favourites_collection.append(book)
    return redirect('/home/favourites')

@app.route('/home/favourites', methods = ["GET"])
def show():
    return render_template('favourites.html', title="Books for Ducks", book_shelves= favourites_collection)

@app.route('/home/delete/<value>', methods = ['POST'])
def remove_book(value):
    collection_of_books.pop(int(value))
    return redirect('/home')

@app.route('/home/<book_ID>', methods = ['GET'])
def individual_item(book_ID):
    return render_template('single_book.html', title="Books for Ducks", item = collection_of_books[int(book_ID)], Book_ID = int(book_ID))

@app.route('/home/<book_ID>', methods = ['POST'])
def check(book_ID):
    box = request.form["box"]
    if box == "listed":
        collection_of_books[int(book_ID)].available = True
    else:
        collection_of_books[int(book_ID)].available = False
    
    return render_template('single_book.html', title="Books for Ducks", item = collection_of_books[int(book_ID)], Book_ID = int(book_ID))

@app.route('/home/thoughts', methods=["POST"])
def add_thoughts():
    return redirect('/home/thoughts', title="Books for Ducks")

@app.route('/home/thoughts', methods=["GET"])
def saved_thoughts():
    return render_template('thoughts.html', title="Books for Ducks")

@app.route('/home/news')
def news():
    return render_template('news.html', title="Books for Ducks")

@app.route('/home/community')
def community():
    return render_template('community.html', title="Books for Ducks")

