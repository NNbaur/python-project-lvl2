import yaml
import json
import os


def restructuring_path(file_name):
    path = os.path.abspath(file_name)
    path = path.split('\\')
    path = '/'.join(path)
    return path


def parse_data(path):
    if '.yml' or '.yaml' in path:
        return yaml.load(open(path), Loader=yaml.FullLoader)
    elif '.json' in path:
        return json.load(open(path))
