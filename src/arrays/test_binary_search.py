from .binary_search import BinarySearch

test_array = [1, 2, 3, 5, 10, 20, 50, 90]
test_case = BinarySearch(test_array)


def test_reverse_array_init() -> None:
    """Check if the class is correctly initializing"""

    assert isinstance(test_case, BinarySearch)


def test_reverse_array_search() -> None:
    """Check if the binary search works as expected"""

    assert test_case.search(5) == 3
    assert test_case.search(50) == 6
    assert test_case.search(4) == -1
    assert test_case.search(100) == -1
