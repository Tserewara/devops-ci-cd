import os
from flask import Flask, render_template
from sqlalchemy.orm import sessionmaker

from database import Post, engine

session = sessionmaker(bind=engine)()

app = Flask(__name__)


@app.route("/")
def home():

    posts = session.query(Post).all()

    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return '<h1>About page</h1>'


@app.route('/contact')
def about():
    return '<h1>Contact page</h1>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
