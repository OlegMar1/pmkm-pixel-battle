from flask import Flask
import os
from src.configurations import Configurations


class PixelBattle:
    def __init__(self, app: Flask):
        configs = Configurations()
        print(configs.html_file_path)

        @app.route("/")
        def index():
            with open(configs.html_file_path, 'r') as html_file:
                page = html_file.read()
                return page
