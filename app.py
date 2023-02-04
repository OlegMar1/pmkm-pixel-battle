from flask import Flask
import argparse

from src.pixel_battle import PixelBattle
from build import Build

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--skip_build', action='store_true')
args = parser.parse_args()

if __name__ == "__main__":
    if not args.skip_build:
        Build()
    app = Flask(
        __name__,
        template_folder='frontend/templates',
        static_folder='frontend/static',
        static_url_path='/',
    )
    PixelBattle(app)
    app.run()


