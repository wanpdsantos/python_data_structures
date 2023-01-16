from .monotonic_check import MonotonicCheck, MonotonicTypes

test_non_increasing = [3, 2, 1]
test_non_decreasing = [1, 2, 3]
test_all_equal = [1, 1, 1]
test_not_monotonic = [1, 3, 2]
test_case = MonotonicCheck()


def test_monotonic_check_init():
    """Check if the class is correctly initializing"""

    assert isinstance(test_case, MonotonicCheck)


def test_monotonic_check():
    """Test for the ordering array process after exponential calculation"""

    assert (
        test_case.check_monotonic(test_non_decreasing)
        == MonotonicTypes.MONOTONIC_NON_DECREASING
    )
    assert (
        test_case.check_monotonic(test_non_increasing)
        == MonotonicTypes.MONOTONIC_NON_INCREASING
    )

    assert (
        test_case.check_monotonic(test_all_equal) == MonotonicTypes.MONOTONIC_ALL_EQUAL
    )

    assert test_case.check_monotonic(test_not_monotonic) == MonotonicTypes.NOT_MONOTONIC
