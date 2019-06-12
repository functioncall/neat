from modules import utils


class File(object):
    """
    File class for any given file
    """
    def __init__(self, file):
        self.original_file      = file
        self.file_copy = file
        self._parsed_file = self._get_parsed_file()
        self.file_name = self.get_file_name()
        self.file_extension = self.get_extension()
        self.file_validity = self.get_file_validity()
        self.file_categorized = False

    def get_instance(self):
        return {
            "original_file": self.original_file,
            "file_name": self.file_name,
            "file_extension": self.file_extension,
            "file_validity": self.file_validity,
            "file_categorized": self.file_categorized
        }

    def _get_parsed_file(self):
        return self.file_copy.split('.')

    def get_file_name(self):
        return self._parsed_file[0]

    def get_extension(self):
        return self._parsed_file[-1].lower()

    def get_file_validity(self):
        if (self.file_name == self.file_extension) or utils.isEmpty(self.file_name):
            return False
        else:
            return True
