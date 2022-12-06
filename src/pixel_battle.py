from flask import Flask, render_template


class PixelBattle:
    def __init__(self, app: Flask):
        @app.route("/")
        def output():
            return render_template('index.html')
