import math


class BinarySearch:
    """Contain the methods to perform a binary search in an ordered array"""

    def __init__(self, input_array: list[int]) -> None:
        self._left_pointer = 0
        self._right_pointer = len(input_array) - 1
        self._middle_pointer = math.floor(self._right_pointer / 2)
        self.array = input_array

    def search(self, searched_value: int) -> int:
        """Search for a given value within the input_array"""

        result_index = -1
        for index in range(0, math.ceil(math.log2(len(self.array)))):
            print(
                "Iter: ",
                index,
                " - Left Pointer: ",
                self._left_pointer,
                " - Right Pointer: ",
                self._right_pointer,
                " - Middle Pointer: ",
                self._middle_pointer,
                " - Search Value: ",
                searched_value,
                " - Current Value: ",
                self.array[self._middle_pointer],
            )

            if searched_value > self.array[self._middle_pointer]:
                self._left_pointer = self._middle_pointer + 1
                self._middle_pointer = math.floor(
                    self._left_pointer
                    + ((self._right_pointer - self._left_pointer) / 2)
                )
            elif searched_value < self.array[self._middle_pointer]:
                self._right_pointer = self._middle_pointer - 1
                self._middle_pointer = math.floor(
                    self._left_pointer
                    + ((self._right_pointer - self._left_pointer) / 2)
                )
            elif searched_value == self.array[self._middle_pointer]:
                result_index = self._middle_pointer
                break
            elif self._left_pointer > self._right_pointer:
                break

        return result_index
