from gendiff.diff_builder.build_diff import create_diff
from gendiff.diff_builder.parse import parse_data, restructuring_path
from gendiff.formatter.format_type import apply_format


def generate_diff(path1: str, path2: str, style: str = 'stylish') -> str:
    file1 = parse_data(restructuring_path(path1))
    file2 = parse_data(restructuring_path(path2))
    diff = create_diff(file1, file2)
    return apply_format(diff, style)
