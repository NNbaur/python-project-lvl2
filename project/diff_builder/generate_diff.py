from project.diff_builder.build_diff import create_diff
from project.diff_builder.parse import parse_data, restructuring_path
from project.formatter import create_stylish


def generate_diff(path1, path2, style=create_stylish):
    file1 = parse_data(restructuring_path(path1))
    file2 = parse_data(restructuring_path(path2))
    diff = create_diff(file1, file2)
    return style(diff)
