from typing import List, TypeVar, Union, cast

"""
Defines function `flatten` which will recursively flatten a list of singleton elements or lists to a depth of 1 (a list of singleton elements).

Note that Python is not the best at recursion. On the author's system, this function cannot handle more than 97 levels of recursion before it will trigger a stack overflow.

This is intended to mimic array behavior, so elements of the list should be of the same type, though, it may work with mixed types.
"""
T = TypeVar("T")

def flatten(deep_arr: List[Union[T, List]]) -> List[T]:
    flat: List[T] = []
    for element in deep_arr:
        if isinstance(element, list):
            flat += flatten(element)
        else:
            element = cast(T, element)
            flat.append(element)
    return flat
