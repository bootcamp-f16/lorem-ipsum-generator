from os import path
from flask import render_template

from app import app
from app.lib.lorem import Lorem

@app.route("/")
@app.route("/index")
def index():
    """
    Opens a file with lorem ipsum words in it.
    Creates a string of lorem ipsum by pulling
    radom words from the input file.

    Displays the string of lorem ipsum to the user
    """

    filepath = path.join(path.dirname(__file__), "data/lorem.txt")
    lorem = Lorem(words_file=filepath)
    lorem_text = lorem.get_lorem_text(200, 500)

    return render_template("index.html", lorem_text=lorem_text)