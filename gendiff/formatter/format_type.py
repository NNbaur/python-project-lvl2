from gendiff.formatter.stylish import create_stylish
from gendiff.formatter.plain import create_plain
from gendiff.formatter.json import create_json


def apply_format(diff: list, style: str) -> str:
    if style == 'stylish':
        return create_stylish(diff)
    elif style == 'plain':
        return create_plain(diff)
    elif style == 'json':
        return create_json(diff)
    raise NameError('Please choose correct format')
