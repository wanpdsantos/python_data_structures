class ReverseArray:
    """Create objects containing methods to reverse array"""

    def __init__(self, input_array: list):
        self.array = input_array

    def reverse(self) -> list:
        """Reverse the input array"""

        reversed_array = []
        for index in range(len(self.array), 0, -1):
            print("index: ", index, " - reversed_array: ", reversed_array)
            reversed_array.append(self.array[index - 1])

        return reversed_array
