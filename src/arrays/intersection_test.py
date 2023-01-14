from .intersection import ArrayIntersection

test_array_ordered_1 = [1, 20, 32, 54, 60]
test_array_ordered_2 = [15, 25, 32, 54]
test_array_unordered_1 = [10, 2, 32, 5]
test_array_unordered_2 = [1, 5, 3, 32]
test_case = ArrayIntersection()


def test_intersection_init() -> None:
    """Check if the class is correctly initializing"""

    assert isinstance(test_case, ArrayIntersection)


def test_intersection_from_unordered() -> None:
    """Check if the binary search works as expected"""

    assert test_case.intersect_from_unordered(
        test_array_unordered_1, test_array_unordered_2
    ) == [32, 5]


def test_intersection_from_ordered() -> None:
    """Check if the binary search works as expected"""

    assert test_case.intersect_from_ordered(
        test_array_ordered_1, test_array_ordered_2
    ) == [32, 54]
