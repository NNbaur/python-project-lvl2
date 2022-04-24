from project.parse import parse_data


def is_bool(argument):
    return str(argument).lower() if type(argument) is bool else argument


def generate_diff(file_path1, file_path2):
    s1 = parse_data(file_path1)
    s2 = parse_data(file_path2)
    set1 = set(s1)
    set2 = set(s2)
    lst = []
    string = ""
    set3 = set1 - set2
    set4 = set2 - set1
    set5 = set1 & set2

    for i in set3:
        lst.append(f'- {i}: {is_bool(s1[i])}')
    for j in set4:
        lst.append(f'+ {j}: {is_bool(s2[j])}')

    for k in set5:
        if s1[k] == s2[k]:
            lst.append(f'  {k}: {is_bool(s1[k])}')
        else:
            lst.append(f'- {k}: {is_bool(s1[k])}')
            lst.append(f'+ {k}: {is_bool(s2[k])}')

    lst.sort(key=lambda x: x[2])

    for i in lst:
        string += '  ' + i + '\n'

    return ('\n' + '{' + '\n' + f'{string}' + '}')
