from typing import List, Union

import pytest

from .array_flatten import flatten


@pytest.mark.parametrize("input,expected_output", [
    ([[1,2,[3]],4], [1,2,3,4]),
    ([[1,2,3,4]], [1,2,3,4]),
    ([[1], [[2, [3, [4]]]]], [1,2,3,4]),
    ([[], [[[[[[[[1], [], 2], 3], 4], 5], 6], 7], 8],], [1,2,3,4,5,6,7,8]),
    ([1,2,3,4], [1,2,3,4]),
    ([], []),
    ([[[[[[]]]]]], []),
])
def test_flatten(input: List, expected_output: List[int]):
    assert flatten(input) == expected_output