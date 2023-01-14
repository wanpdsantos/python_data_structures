from .missing_elements import MissingElements


def test_check_missing_elements_from_ordered_array():
    """Check if the missing elements method is working properly"""

    assert MissingElements().check_missing_elements_from_ordered_array(
        [1, 2, 3, 5]
    ) == [4]

    assert MissingElements().check_missing_elements_from_ordered_array(
        [1, 2, 3, 5, 6, 7, 10, 13]
    ) == [4, 8, 9, 11, 12]
