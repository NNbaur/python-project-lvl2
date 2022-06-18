from gendiff.diff_builder.generate_diff import generate_diff
from gendiff.diff_builder.parse import parse_data
from tests.test_parse import get_path
import json


def test_gen_diff_json():
    path_res1 = get_path('result_test1.json')
    expected_res1 = parse_data(path_res1)
    result1 = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json')
    assert result1 == expected_res1
    path_res2 = get_path('result_test2.json')
    expected_res2 = parse_data(path_res2)
    result2 = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/empty_dict.json')
    assert result2 == expected_res2


def test_gen_diff_yml():
    path_res1 = get_path('result_test_yml1.yml')
    expected_res1 = parse_data(path_res1)
    result1 = generate_diff(
        'tests/fixtures/filepath1.yml',
        'tests/fixtures/filepath2.yml')
    assert result1 == expected_res1
    path_res2 = get_path('result_test_yml2.yml')
    expected_res2 = parse_data(path_res2)
    result2 = generate_diff(
        'tests/fixtures/filepath1.yml',
        'tests/fixtures/filepath_empty.yml')
    assert result2 == expected_res2


def test_gen_diff_ts():
    path_res1 = get_path('result_test_yml3.yml')
    expected_res1 = parse_data(path_res1)
    result1 = generate_diff(
        'tests/fixtures/filepath3.yml',
        'tests/fixtures/filepath4.yml')
    assert result1 == expected_res1
    path_res2 = get_path('result_test_yml4.yml')
    expected_res2 = parse_data(path_res2)
    result2 = generate_diff(
        'tests/fixtures/filepath3.yml',
        'tests/fixtures/filepath_empty.yml')
    assert result2 == expected_res2


def test_gen_diff_ts_plain():
    path_res1 = get_path('result_plain1.json')
    expected_res1 = parse_data(path_res1)
    result1 = generate_diff(
        'tests/fixtures/filepath3.yml',
        'tests/fixtures/filepath4.yml', 'plain')
    assert result1 == expected_res1
    path_res2 = get_path('result_plain2.json')
    expected_res2 = parse_data(path_res2)
    result2 = generate_diff(
        'tests/fixtures/filepath3.yml',
        'tests/fixtures/filepath_empty.yml', 'plain')
    assert result2 == expected_res2


def test_gen_diff_ts_json():
    path_res1 = get_path('result_json.json')
    expected_res1 = json.dumps(parse_data(path_res1), indent=4)
    result1 = generate_diff(
        'tests/fixtures/filepath3.json',
        'tests/fixtures/filepath4.json', 'json')
    assert result1 == expected_res1
