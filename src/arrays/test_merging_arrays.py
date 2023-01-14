from .merging_arrays import MergeArray

test_array = [1, 2, 50, 90]
test_case = MergeArray(test_array)


def test_merge_arrays_init() -> None:
    """Check if the class is correctly initializing"""

    assert isinstance(test_case, MergeArray)


def test_merging_arrays_merge() -> None:
    """Check if the merge method works as expected"""

    assert test_case.merge([10, 95]) == [1, 2, 10, 50, 90, 95]
    assert test_case.merge([-4, 15]) == [-4, 1, 2, 15, 50, 90]
