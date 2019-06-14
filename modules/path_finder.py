
from modules import utils


def _category_is_found(file_extension, current_extension_list):
    if file_extension in current_extension_list:
        return True
    else:
        return False


def _get_path(file, config):
    for category, category_config in config.items():
        current_file_extension      = file["file_extension"]
        current_extension_list      = category_config["extension_list"]
        current_subfolders          = category_config["subfolders"]

        if _category_is_found(current_file_extension, current_extension_list):
            if not utils.isEmpty(current_subfolders):
                return category + "/" + recursively_compute_path(file, current_subfolders)
            else:
                file["file_categorized"] = True
                return category + "/"
    return ""


def recursively_compute_path(file, config):
    path = _get_path(file, config)

    if not file["file_validity"] or (not file["file_categorized"]):
        return "others/"
    else:
        return path


def find_path(file, config):
    """
    Recursively compute file path from config
    :param file:
    :param config:
    :return:
    """

    return recursively_compute_path(file, config)
