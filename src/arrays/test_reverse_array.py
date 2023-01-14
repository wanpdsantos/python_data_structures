from .reverse_array import ReverseArray


def test_reverse_array_init():
    """Check if the class is correctly initializing"""
    test_array = [1, 2, 3]
    test_case = ReverseArray(test_array)
    assert isinstance(test_case, ReverseArray)


def test_reverse_array():
    """Test for the ordering array process after exponential calculation"""
    test_array = [1, 2, 3]
    test_case = ReverseArray(test_array)
    assert test_case.reverse() == [3, 2, 1]
