import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    answer = generate_diff(args.first_file, args.second_file)
    print(answer)



def generate_diff(file_path1, file_path2):
    s1 = json.load(open(file_path1))
    s2 = json.load(open(file_path2))
    set1 = set(s1)
    set2 = set(s2)
    lst = []
    string = ""

    set3 = set1 - set2
    set4 = set2 - set1
    set5 = set1 & set2

    for i in set3:
        lst.append(f'- {i}: {s1[i]}')
    for j in set4:
        lst.append(f'+ {j}: {s2[j]}')

    for k in set5:
        if s1[k] == s2[k]:
            lst.append(f'  {k}: {s1[k]}')
        else:
            lst.append(f'- {k}: {s1[k]}')
            lst.append(f'+ {k}: {s2[k]}')

    lst.sort(key=lambda x: x[2])

    for i in lst:
        string += '  ' + i + '\n'

    return ('\n' +'{' + '\n' + f'{string.lower()}' + '}')

if __name__ == '__main__':
    main()