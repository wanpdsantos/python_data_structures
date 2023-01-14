class MissingElements:
    """Contains the methods to find missing elements in an array"""

    def __init__(self) -> None:
        pass

    def check_missing_elements_from_ordered_array(self, input_array: list[int]):
        """Check for missing element in a list of ordered integers"""

        difference_between_index_and_element = input_array[0]
        missing_elements = []
        for index, element in enumerate(input_array):
            if element - index != difference_between_index_and_element:
                # required when multiple elements in sequence are missing
                for missing in range(
                    difference_between_index_and_element, element - index
                ):
                    missing_elements.append(missing + index)

                difference_between_index_and_element = element - index
        return missing_elements

    def check_missing_elements_from_unordered_array(
        self, input_array: list[int]
    ) -> list[int]:
        """Check for missing element in a list of ordered integers"""

        hashmap = [0 for elem in range(0, max(input_array))]
        missing_elements = []
        for element in input_array:
            hashmap[element - 1] = 1
        for index, element in enumerate(hashmap):
            if element == 0:
                missing_elements.append(index + 1)
        return missing_elements
