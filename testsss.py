from gendiff.diff_builder.generate_diff import generate_diff
from gendiff.diff_builder.parse import parse_data, restructuring_path

a = generate_diff('tests/fixtures/filepath3.yml', 'tests/fixtures/filepath4.yml', 'plain')
print(a)