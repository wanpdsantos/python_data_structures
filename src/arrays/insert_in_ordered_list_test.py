from .insert_in_ordered_list import InsertInOrderedList

test_array = [1, 2, 50, 90]
test_case = InsertInOrderedList(test_array)


def test_reverse_array_init() -> None:
    """Check if the class is correctly initializing"""

    assert isinstance(test_case, InsertInOrderedList)


def test_insert_in_ordered_list_insert() -> None:
    """Check if the insert method works as expected"""

    assert test_case.insert(15) == [1, 2, 15, 50, 90]
    assert test_case.insert(-4) == [-4, 1, 2, 15, 50, 90]
    assert test_case.insert(100) == [-4, 1, 2, 15, 50, 90, 100]
