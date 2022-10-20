from flask import Flask
import os

FRONTEND_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'frontend')
)
HTML_FILE_PATH = os.path.join(
    FRONTEND_PATH,
    'index.html'
)

app = Flask(__name__)


@app.route("/")
def index():
    with open(HTML_FILE_PATH, 'r') as html_file:
        page = html_file.read()
        return page


if __name__ == "__main__":
    app.run()
