from enum import Enum


class MonotonicTypes(Enum):
    """Types of monotonic arrays"""

    NOT_MONOTONIC = "NOT_MONOTONIC"
    MONOTONIC_NON_INCREASING = "MONOTONIC_NON_INCREASING"
    MONOTONIC_NON_DECREASING = "MONOTONIC_NON_DECREASING"
    MONOTONIC_ALL_EQUAL = "MONOTONIC_ALL_EQUAL"


class MonotonicCheck:
    """Contains methods to check if the array is monotonic"""

    def __init__(self) -> None:
        pass

    def check_monotonic(self, input_array: list[int]) -> MonotonicTypes:
        """Check if the array is monotonic increasing or decreasing"""

        monotonic_flag = MonotonicTypes.NOT_MONOTONIC
        if input_array[0] < input_array[-1]:
            monotonic_flag = MonotonicTypes.MONOTONIC_NON_DECREASING
        elif input_array[0] > input_array[-1]:
            monotonic_flag = MonotonicTypes.MONOTONIC_NON_INCREASING
        elif input_array[0] == input_array[-1]:
            monotonic_flag = MonotonicTypes.MONOTONIC_ALL_EQUAL

        for index in range(0, len(input_array) - 1):
            if (
                input_array[index] > input_array[index + 1]
                and monotonic_flag == MonotonicTypes.MONOTONIC_NON_DECREASING
            ) or (
                input_array[index] < input_array[index + 1]
                and monotonic_flag == MonotonicTypes.MONOTONIC_NON_INCREASING
            ):
                monotonic_flag = MonotonicTypes.NOT_MONOTONIC

        return monotonic_flag
