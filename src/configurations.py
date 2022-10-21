import os


class Configurations:
    def __init__(self):
        frontend_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'frontend')
        )
        self.html_file_path = os.path.join(
            frontend_path,
            'index.html'
        )
