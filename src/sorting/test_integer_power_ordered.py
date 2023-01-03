from .integer_power_ordered import IntegerOrderedSorting


def test_integer_ordered_sorting_init():
    """Check if the class is correctly initializing"""

    test_array = [1, 2, 3]
    test_case = IntegerOrderedSorting(test_array)
    assert isinstance(test_case, IntegerOrderedSorting)


def test_power_and_sort():
    """Test for the ordering array process after exponential calculation"""

    test_arrays = [
        {"input": [1, 2, 3, 4, 5], "output": [1, 4, 9, 16, 25]},
        {"input": [-5, -4, 1, 2, 3], "output": [1, 4, 9, 16, 25]},
    ]
    for array in test_arrays:
        sorting_check = IntegerOrderedSorting(array["input"])
        assert sorting_check.power_and_sort(2) == array["output"]
