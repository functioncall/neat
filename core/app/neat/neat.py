import os

from core.app_interface.i_app import App
from pathlib import Path
from common import config
from modules import cleaner


class Neat(App):
    # Initialize app
    def __init__(self):
        self._setup()

    def _setup(self):
        self._setup_config()
        self._setup_paths()
        self._setup_files()
        self._setup_cleaner()

    def _setup_paths(self):
        self.home_dir           = str(Path.home())
        self.source_directory   = self.home_dir + "/Downloads/"
        self.target_directory   = self.home_dir + "/Desktop/MyFiles/"

    def _setup_config(self):
        self.config             = config.configurations["root"]

    def _setup_files(self):
        self.files              = [x for x in os.walk(self.source_directory)][0][2]

    def _setup_cleaner(self):
        self.cleaner            = cleaner.Cleaner(
                                    self.source_directory,
                                    self.target_directory,
                                    self.config)

    def execute(self):
        for file in self.files:
            self.cleaner.clean(file)
