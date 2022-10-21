from flask import Flask

from src.pixel_battle import PixelBattle
if __name__ == "__main__":
    app = Flask(__name__)
    PixelBattle(app)
    app.run()
