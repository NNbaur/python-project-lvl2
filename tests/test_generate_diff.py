from project.generate_diff import generate_diff
import json
import os


def restructuring_path(file_name):
    path = os.path.abspath(f'tests/fixtures/{file_name}')
    path = path.split('\\')
    path = '/'.join(path)
    return path


def test_generate_diff1():
    path_res1 = restructuring_path('result_test1.json')
    expected_res1 = json.load(open(path_res1))
    path_t1 = restructuring_path('file1.json')
    path_t2 = restructuring_path('file2.json')
    result1 = generate_diff(path_t1, path_t2)
    assert result1 == expected_res1
    path_res2 = restructuring_path('result_test2.json')
    expected_res2 = json.load(open(path_res2))
    path_t3 = restructuring_path('file1.json')
    path_t4 = restructuring_path('empty_dict.json')
    result2 = generate_diff(path_t3, path_t4)
    assert result2 == expected_res2

