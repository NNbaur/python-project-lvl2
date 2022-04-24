import yaml
import json


def parse_data(path):
    if '.yml' or '.yaml' in path:
        return yaml.load(open(path), Loader=yaml.FullLoader)
    elif '.json' in path:
        return json.load(open(path))
