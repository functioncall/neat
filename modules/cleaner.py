import os

from shutil import copyfile
from modules import utils
from modules import path_finder


class Cleaner:
    def __init__(self, source_directory, base_target_directory, config):
        self.source_directory       = source_directory
        self.base_target_directory  = base_target_directory
        self.config                 = config

    def clean(self, item):
        return self._clean_and_copy(item)

    def _clean_and_copy(self, item):
        """
        Function which copies item for a source dir to a target dir
        :param item:
        :return:
        """
        source_file_path         = self._get_source_file_path(item)
        target_file_path         = self._get_target_file_path(item)

        return copyfile(source_file_path, target_file_path)

    def _clean_and_clear(self, item):
        """
        Function which deletes item from a source dir and moves it to a target dir
        :param item:
        :return:
        """
        source_file_path         = self._get_source_file_path(item)
        target_file_path         = self._get_target_file_path(item)

        pass  # add missing implementation for moving files

    def _get_source_file_path(self, item):
        return self.source_directory + item

    def _get_target_file_path(self, item):
        target_dir               = self._get_target_directory_path(item)

        return target_dir + item

    def _get_target_directory_path(self, item):
        file                     = self.get_source_file_details(item)
        target_directory_path    = self._generate_target_dir_path(file)

        return target_directory_path

    def _generate_target_dir_path(self, file):
        target_dir_path = self._find_target_dir_path(file)

        if not os.path.exists(target_dir_path):
            os.makedirs(target_dir_path)

        return target_dir_path

    def _find_target_dir_path(self, file):
        return self.base_target_directory + path_finder.find_path(file, self.config)

    @staticmethod
    def get_source_file_details(item):
        return utils.get_details(item)
