from .missing_elements import MissingElements


def test_check_missing_elements_from_ordered_array():
    """Check if the missing elements method is working properly given ordered array"""

    assert MissingElements().check_missing_elements_from_ordered_array(
        [1, 2, 3, 5]
    ) == [4]

    assert MissingElements().check_missing_elements_from_ordered_array(
        [1, 2, 3, 5, 6, 7, 10, 13]
    ) == [4, 8, 9, 11, 12]


def test_check_missing_elements_from_unordered_array():
    """Check if the missing elements method is working properly given unordered array"""

    assert MissingElements().check_missing_elements_from_unordered_array(
        [1, 2, 3, 5, 6, 7, 10, 13]
    ) == [4, 8, 9, 11, 12]

    assert MissingElements().check_missing_elements_from_unordered_array(
        [5, 1, 7, 3, 6, 10, 13, 2]
    ) == [4, 8, 9, 11, 12]
