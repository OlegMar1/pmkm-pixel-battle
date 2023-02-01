import os
import shutil
import argparse
from src.configurations import Configurations


class Build:
    def __init__(self):
        configs = Configurations()
        os.system(f'cmd /c "cd frontend\\angular & npm install & ng b"')

        # if not os.path.exists(configs.static_folder_path):
        #     os.mkdir(configs.static_folder_path)
        # else:
        #     shutil.rmtree(configs.static_folder_path)
        #     os.rmdir(configs.static_folder_path)
        #     os.mkdir(configs.static_folder_path)
        #
        # if not os.path.exists(configs.templates_folder_path):
        #     os.mkdir(configs.templates_folder_path)
        # else:
        #     shutil.rmtree(configs.templates_folder_path)
        #     os.rmdir(configs.templates_folder_path)
        #     os.mkdir(configs.static_folder_path)

        if os.path.exists(configs.static_folder_path):
            shutil.rmtree(configs.static_folder_path)

        if os.path.exists(configs.templates_folder_path):
            shutil.rmtree(configs.templates_folder_path)

        os.mkdir(configs.static_folder_path)
        os.mkdir(configs.templates_folder_path)

        static_files_list = []
        template_files_list = []
        for file in os.listdir(configs.builded_files_path):
            if file.endswith('.js') or file.endswith('.css'):
                static_files_list.append(
                    os.path.join(
                        configs.builded_files_path,
                        file
                    )
                )
            elif file.endswith('.html'):
                template_files_list.append(
                    os.path.join(
                        configs.builded_files_path,
                        file
                    )
                )

        if static_files_list:
            for file in static_files_list:
                shutil.copy2(file, configs.static_folder_path)
        if template_files_list:
            for file in template_files_list:
                shutil.copy2(file, configs.templates_folder_path)
