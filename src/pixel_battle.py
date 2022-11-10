from flask import Flask, render_template
import os
from src.configurations import Configurations


class PixelBattle:
    def __init__(self, app: Flask):
        configs = Configurations()
        print(configs.html_file_path)

        @app.route("/")
        def output():
            return render_template('index.html')
