def stylish(dict1, depth=2):
    result = ''
    lst = list(map(lambda x: x, dict1))
    lst.sort(key=lambda x: x[2:])
    for i in lst:
        if type(dict1[i]) is dict:
            result += '\n' + depth * " " + f'{i}:'
            f' {stylish(dict1[i], depth + 4)}'
        else:
            result += '\n' + depth * " " + f'{i}: {str(dict1[i])}'
    return '{' + result + '\n' + (depth - 2) * " " + '}'
