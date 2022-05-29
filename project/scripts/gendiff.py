#!/usr/bin/env python
import argparse
from project.diff_builder.generate_diff import generate_diff
from project.formatter import create_stylish


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        default=create_stylish
    )

    args = parser.parse_args()
    answer = generate_diff(
        args.first_file,
        args.second_file,
        args.format)
    print(answer)


if __name__ == '__main__':
    main()
