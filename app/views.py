from os import path
from random import choice, randint
from flask import render_template

from app import app

@app.route("/")
@app.route("/index")
def index():
    """
    Opens a file with lorem ipsum words in it.
    Creates a string of lorem ipsum by pulling
    radom words from the input file.

    Displays the string of lorem ipsum to the user
    """
    lorem_filepath = path.join(path.dirname(__file__), "data/lorem.txt")

    with open(lorem_filepath, 'r') as lorem_file:
        all_lorem_text = lorem_file.read()

    words = all_lorem_text.split(" ")
    num_words = randint(50, 200)
    selected_words = [choice(words) for x in range(num_words)]
    lorem_text = " ".join(selected_words)

    return render_template("index.html", lorem_text=lorem_text)