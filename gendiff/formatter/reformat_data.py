from typing import Any


def is_none(function):
    def inner(arg):
        result = function(arg)
        return 'null' if result == 'None' or result == "'None'" else result
    return inner


@is_none
def is_bool_or_int(arg: Any) -> Any:
    return str(arg).lower() if isinstance(arg, bool)\
        else arg if isinstance(arg, int) else f"'{arg}'"


@is_none
def is_bool(arg: Any) -> str:
    return str(arg).lower() if isinstance(arg, bool) else str(arg)
