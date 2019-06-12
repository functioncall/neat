import os

from shutil import copyfile
from modules import utils
from modules import path_finder


class Cleaner:
    def __init__(self, source_directory, target_directory, config):
        self.source_directory = source_directory
        self.target_directory = target_directory
        self.config           = config

    def clean(self, item):
        return self.clean_and_copy(item)

    def clean_and_copy(self, item):
        """
        Function which copies item for a source dir to a target dir
        :param item:
        :return:
        """
        target_dir       = self.get_target_directory_path(item)

        source_file_path = self.source_directory + item
        target_file_path = target_dir + item
        return copyfile(source_file_path, target_file_path)

    def clean_and_clear(self, item):
        """
        Function which deletes item from a source dir and moves it to a target dir
        :param item:
        :return:
        """
        pass # adding missing implementation

    def get_target_directory_path(self, item):
        file                     = utils.get_details(item)
        target_directory_path    = self.target_directory + path_finder.get_target_file_path(self.config, file)

        if not os.path.exists(target_directory_path):
            os.makedirs(target_directory_path)

        return target_directory_path
