def stylish(dict1, depth=2):
    res = ''
    lst = list(map(lambda x: x, dict1))
    lst.sort(key=lambda x: x[2:])
    for i in lst:
        if type(dict1[i]) is dict:
            res += '\n' + depth * " " + f'{i}: {stylish(dict1[i], depth + 4)}'
        else:
            res += '\n' + depth * " " + f'{i}: {str(dict1[i])}'
    return '{' + res + '\n' + (depth - 2) * " " + '}'
