from project.generate_diff import generate_diff
from project.parse import parse_data
import os


def restructuring_path(file_name):
    path = os.path.abspath(f'tests/fixtures/{file_name}')
    path = path.split('\\')
    path = '/'.join(path)
    return path


def test_gen_diff_json():
    path_res1 = restructuring_path('result_test1.json')
    expected_res1 = parse_data(path_res1)
    path_t1 = restructuring_path('file1.json')
    path_t2 = restructuring_path('file2.json')
    result1 = generate_diff(path_t1, path_t2)
    assert result1 == expected_res1
    path_res2 = restructuring_path('result_test2.json')
    expected_res2 = parse_data(path_res2)
    path_t3 = restructuring_path('file1.json')
    path_t4 = restructuring_path('empty_dict.json')
    result2 = generate_diff(path_t3, path_t4)
    assert result2 == expected_res2


def test_gen_diff_yml():
    path_res1 = restructuring_path('result_test_yml1.yml')
    expected_res1 = parse_data(path_res1)
    path_t1 = restructuring_path('filepath1.yml')
    path_t2 = restructuring_path('filepath2.yml')
    result1 = generate_diff(path_t1, path_t2)
    assert result1 == expected_res1
    path_res2 = restructuring_path('result_test_yml2.yml')
    expected_res2 = parse_data(path_res2)
    path_t3 = restructuring_path('file1.json')
    path_t4 = restructuring_path('empty_dict.json')
    result2 = generate_diff(path_t3, path_t4)
    assert result2 == expected_res2

