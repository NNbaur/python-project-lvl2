import os


def get_path(filename):
    path = os.path.abspath(f'tests/fixtures/{filename}')
    path = path.split('\\')
    path = '/'.join(path)
    return path
