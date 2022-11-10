from flask import Flask

from src.pixel_battle import PixelBattle
if __name__ == "__main__":
    app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')
    PixelBattle(app)
    app.run()
