from gendiff.diff_builder.build_diff import get_diff_type, get_key,\
    get_value, get_child
from typing import Any


def reformat_collection(
        diff: list,
        depth: int,
        spaces: str,
        collection: list
) -> list:

    for tree in diff:
        diff_type = get_diff_type(tree)
        key = get_key(tree)
        diff_value = get_value(tree)
        child = get_child(tree)

        if diff_type == 'deleted':
            string = create_string(
                spaces,
                '-',
                key,
                create_value(
                    diff_value[0],
                    depth + 1,
                ),
            )

        elif diff_type == 'added':
            string = create_string(
                spaces,
                '+',
                key,
                create_value(
                    diff_value[0],
                    depth + 1,
                ),
            )

        elif diff_type == 'unchanged':
            string = create_string(
                spaces,
                ' ',
                key,
                create_value(
                    diff_value[0],
                    depth + 1,
                ),
            )

        elif diff_type == 'child':
            string = create_string(
                spaces,
                ' ',
                key,
                create_stylish(
                    child,
                    depth + 1,
                ),
            )

        else:
            string_old = create_string(
                spaces,
                '-',
                key,
                create_value(
                    diff_value[0],
                    depth + 1,
                ),
            )
            string_new = create_string(
                spaces,
                '+',
                key,
                create_value(
                    diff_value[1],
                    depth + 1,
                ),
            )
            string = '{0}\n{1}'.format(string_old, string_new)
        collection.append(string)
    return collection


def is_none(function):
    def inner(arg):
        result = function(arg)
        return 'null' if result == 'None' else result
    return inner


@is_none
def is_bool(arg: Any) -> str:
    return str(arg).lower() if isinstance(arg, bool) else str(arg)


def create_value(diff_value: Any, depth: int) -> str:
    template = []
    count = 4 * depth - 2
    spaces = ' ' * count

    if isinstance(diff_value, dict):
        template.append('{')
        for key, dict_value in diff_value.items():
            template.append(
                create_string(
                    spaces,
                    ' ',
                    key,
                    create_value(
                        dict_value,
                        depth + 1,
                    ),
                ),
            )
        template.append('{0}}}'.format(' ' * (count - 2)))
    else:
        template.append(is_bool(diff_value))

    return '\n'.join(template)


def create_string(spaces: str, symbol: str, key: Any, diff_value: Any) -> str:
    return '{0}{1} {2}: {3}'.format(
        spaces,
        symbol,
        key,
        diff_value,
    )


def create_stylish(diff: list, depth: int = 1) -> str:
    collection = []
    collection.append('{')
    count = 4 * depth - 2
    spaces = ' ' * count
    collection = reformat_collection(diff, depth, spaces, collection)
    collection.append('{0}}}'.format(' ' * (count - 2)))
    return '\n'.join(collection)
