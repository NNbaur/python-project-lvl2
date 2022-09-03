import json


def create_json(diff: list) -> str:
    return json.dumps(diff, indent=4)
