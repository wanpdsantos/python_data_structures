class InsertInOrderedList:
    """Defines the methods to insert a new element in a sorted list"""

    def __init__(self, input_array: list[int]) -> None:
        self.array = input_array

    def insert(self, value_to_insert: int) -> list[int]:
        """Insert a new element in the array"""
        right_pointer = len(self.array) - 1
        if self.array[right_pointer] < value_to_insert:
            self.array.append(value_to_insert)
            return self.array

        while self.array[right_pointer] > value_to_insert and right_pointer >= 0:
            print(
                "Right Pointer: ",
                right_pointer,
                " - Result Array: ",
                self.array,
                " - Current Value: ",
                self.array[right_pointer],
                "Value to Insert: ",
                value_to_insert,
            )
            if right_pointer == len(self.array) - 1:
                self.array.append(self.array[right_pointer])
            else:
                self.array[right_pointer + 1] = self.array[right_pointer]
            right_pointer -= 1
        self.array[right_pointer + 1] = value_to_insert
        return self.array
