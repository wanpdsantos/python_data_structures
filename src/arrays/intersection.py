class ArrayIntersection:
    """Contains methods to perform intersection operation on arrays"""

    def __init__(self) -> None:
        pass

    def intersect_from_unordered(
        self, array1: list[int], array2: list[int]
    ) -> list[int]:
        """Returns the intersection between unordered arrays"""
        result_array = []
        for element_arr1 in array1:
            for element_arr2 in array2:
                if element_arr2 == element_arr1:
                    result_array.append(element_arr1)
                    break
        return result_array

    def intersect_from_ordered(self, array1: list[int], array2: list[int]) -> list[int]:
        """Returns the intersection between ordered arrays"""

        index_arr_1 = 0
        index_arr_2 = 0
        result_array = []
        while index_arr_1 < len(array1) and (index_arr_2 < len(array2)):
            if array1[index_arr_1] > array2[index_arr_2]:
                index_arr_2 += 1
            elif array1[index_arr_1] < array2[index_arr_2]:
                index_arr_1 += 1
            elif array1[index_arr_1] == array2[index_arr_2]:
                result_array.append(array1[index_arr_1])
                index_arr_1 += 1
                index_arr_2 += 1

        return result_array
