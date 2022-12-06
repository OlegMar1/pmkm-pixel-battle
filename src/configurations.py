import os


class Configurations:
    def __init__(self):
        self.frontend_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'frontend')
        )
        self.angular_project_path = os.path.join(self.frontend_path, 'angular')
        self.static_folder_path = os.path.join(self.frontend_path, 'static')
        self.templates_folder_path = os.path.join(self.frontend_path, 'templates')
        self.builded_files_path = os.path.join(self.angular_project_path, 'dist', 'angular')
