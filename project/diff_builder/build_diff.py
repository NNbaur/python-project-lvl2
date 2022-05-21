from project.diff_builder.parse import restructuring_path, parse_data


def is_none(function):
    def inner(argument):
        result = function(argument)
        return 'null' if result is None else result
    return inner


@is_none
def is_bool1(argument):
    return str(argument).lower() if type(argument) is bool else argument


def collect_diff_types(file1, file2):
    set1 = set(file1)
    set2 = set(file2)
    deleted = set1 - set2
    added = set2 - set1
    unchanged = set1 & set2
    return deleted, added, unchanged


def get_children(value):
    dictionary = dict()

    def inner(dictionary):
        if type(value) is dict:
            for k, v in value.items():
                if type(v) is dict:
                    dictionary[f'  {k}'] = get_children(v)
                else:
                    dictionary[f'  {k}'] = is_bool1(v)
        return dictionary
    return inner(dictionary)


def diff_deleted(collection, file, dictionary):
    for i in collection:
        if type(file[i]) is dict:
            dictionary[f'- {i}'] = get_children(file[i])
        else:
            dictionary[f'- {i}'] = is_bool1(file[i])
    return dictionary


def diff_added(collection, file, dictionary):
    for j in collection:
        if type(file[j]) is dict:
            dictionary[f'+ {j}'] = get_children(file[j])
        else:
            dictionary[f'+ {j}'] = is_bool1(file[j])
    return dictionary


def diff_unchanged(collection, file1, file2, inner, dict1):
    for k in collection:
        if type(file1[k]) is dict and type(file2[k]) is dict:
            dict1[f'  {k}'] = inner(file1[k], file2[k])
        elif file1[k] == file2[k]:
            dict1[f'  {k}'] = is_bool1(file1[k])
        else:
            if type(file1[k]) is dict:
                dict1[f'- {k}'] = get_children(file1[k])
            else:
                dict1[f'- {k}'] = is_bool1(file1[k])
            if type(file2[k]) is dict:
                dict1[f'+ {k}'] = get_children(file2[k])
            else:
                dict1[f'+ {k}'] = is_bool1(file2[k])
    return dict1


def create_diff(file1, file2):

    def inner(file1, file2):
        dict1 = dict()
        col1, col2, col3 = collect_diff_types(file1, file2)
        diff_deleted(col1, file1, dict1)
        diff_added(col2, file2, dict1)
        diff_unchanged(col3, file1, file2, inner, dict1)
        return dict1
    return inner(file1, file2)