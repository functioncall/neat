
from modules import utils


def _category_is_found(file_extension, current_extension_list):
    if file_extension in current_extension_list:
        return True
    else:
        return False


def _get_path(root, file):
    for category, category_config in root.items():
        current_extension_list      = category_config["extension_list"]
        current_subfolders          = category_config["subfolders"]
        current_file_extension      = file["file_extension"]

        if _category_is_found(current_file_extension, current_extension_list):
            if not utils.isEmpty(current_subfolders):
                return category + "/" + get_target_file_path(current_subfolders, file)
            else:
                file["file_categorized"] = True
                return category + "/"

    return ""


def get_target_file_path(root, file):
    path = _get_path(root, file)
    if not file["file_validity"] or (not file["file_categorized"]):
        return "others/"
    else:
        return path
