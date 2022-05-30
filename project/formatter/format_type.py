from project.formatter.stylish import create_stylish
from project.formatter.plain import create_plain


def apply_format(diff, style):
    if style == 'stylish':
        return create_stylish(diff)
    elif style == 'plain':
        return create_plain(diff)
    raise NameError('Please choose correct format')
