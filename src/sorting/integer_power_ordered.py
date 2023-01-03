class IntegerOrderedSorting:
    """Power of each element of the array and sort in ascending order. Input array must already be sorted"""

    def __init__(self, input_array: list):
        self._array = input_array
        self._right_pointer = len(input_array) - 1
        self._left_pointer = 0
        self._result_array = [0 for elem in input_array]

    def _decrement_right_pointer(self) -> None:
        """Method to decrease the right pointer"""

        self._right_pointer -= 1

    def _increment_left_pointer(self) -> None:
        """Method to increase the left pointer"""

        self._left_pointer += 1

    def power_and_sort(self, power_index: int) -> list:
        """Power of each element of the array and sort in ascending order."""

        for idx in range(len(self._array)):
            print(
                "Iter: ",
                idx,
                " - Left Pointer: ",
                self._left_pointer,
                " - Right Pointer: ",
                self._right_pointer,
                " - Result Array: ",
                self._result_array,
            )
            right_pointer_pow = pow(self._array[self._right_pointer], power_index)
            left_pointer_pow = pow(self._array[self._left_pointer], power_index)
            if left_pointer_pow >= right_pointer_pow:
                self._result_array[
                    self._right_pointer - self._left_pointer
                ] = left_pointer_pow
                self._increment_left_pointer()
            else:
                self._result_array[
                    self._right_pointer - self._left_pointer
                ] = right_pointer_pow
                self._decrement_right_pointer()
        return self._result_array
