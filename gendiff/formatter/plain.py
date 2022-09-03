from gendiff.diff_builder.build_diff import get_diff_type, get_key,\
    get_value, get_child
from typing import Any


def create_plain(diff: list, path=[]) -> str:
    collection = []
    for tree in diff:
        diff_type = get_diff_type(tree)
        key = get_key(tree)
        diff_value = get_value(tree)
        child = get_child(tree)
        path.append(key)

        if diff_type == 'added':
            collection.append(
                create_string(
                    "Property '{path}' was added with value: {value}",
                    path,
                    diff_value[0]
                )
            )
        elif diff_type == 'deleted':
            collection.append(
                create_string(
                    "Property '{path}' was removed",
                    path,
                    diff_value[0]
                )
            )
        elif diff_type == 'child':
            collection.append(create_plain(child, path))
        elif diff_type == 'changed':
            collection.append(
                create_string(
                    "Property '{path}' was updated. From {value1} to {value2}",
                    path,
                    diff_value[0],
                    diff_value[1]
                )
            )
        path.pop()
    return '\n'.join(collection)


def is_none1(function):
    def inner(arg):
        result = function(arg)
        return 'null' if result == "'None'" else result
    return inner


@is_none1
def is_bool1(arg: Any) -> Any:
    return str(arg).lower() if isinstance(arg, bool)\
        else arg if isinstance(arg, int) else f"'{arg}'"


def create_value(diff_value: Any) -> Any:
    if isinstance(diff_value, dict):
        diff_value = '[complex value]'
    else:
        diff_value = is_bool1(diff_value)
    return diff_value


def create_string(template: str, path: list, value1: Any, value2=None) -> str:
    if template == "Property '{path}' was updated. " \
                   "From {value1} to {value2}":
        return template.format(
            path='.'.join(path),
            value1=create_value(value1),
            value2=create_value(value2)
        )
    return template.format(
        path='.'.join(path),
        value=create_value(value1)
    )
