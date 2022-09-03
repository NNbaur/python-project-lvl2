from typing import Any


def build_diff_structure(
    diff_type: str,
    key: str,
    value_old: Any,
    value_new=None,
    child=None,
) -> dict:

    return {
        'diff_type': diff_type,
        'key': key,
        'value_old': value_old,
        'value_new': value_new,
        'child': child,
    }


def fill_diff(key: Any, dict1: dict, dict2: dict) -> dict:
    if key not in dict1:
        collection = build_diff_structure(
            'added',
            key,
            dict2[key],
        )
    elif key not in dict2:
        collection = build_diff_structure(
            'deleted',
            key,
            dict1[key],
        )
    elif dict1[key] == dict2[key]:
        collection = build_diff_structure(
            'unchanged',
            key,
            dict1[key],
        )
    elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
        collection = build_diff_structure(
            'child',
            key,
            value_old=None,
            child=create_diff(
                dict1[key],
                dict2[key],
            ),
        )
    else:
        collection = build_diff_structure(
            'changed',
            key,
            value_old=dict1[key],
            value_new=dict2[key],
        )
    return collection


def create_diff(file1: dict, file2: dict) -> list:
    keys = file1.keys() | file2.keys()
    diff = []
    for key in sorted(keys):
        diff.append(fill_diff(key, file1, file2))
    return diff


def get_diff_type(collection: dict) -> str:
    return collection['diff_type']


def get_key(collection: dict) -> Any:
    return collection['key']


def get_value(collection: dict) -> tuple:
    return (collection['value_old'], collection['value_new'])


def get_child(collection: dict) -> list:
    return collection['child']
