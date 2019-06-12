from models import file as F


def isEmpty(obj):
    return obj == {} or obj == ""


def get_details(item):
    return F.File(item).get_instance()
