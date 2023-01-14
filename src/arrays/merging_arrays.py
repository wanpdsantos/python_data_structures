class MergeArray:
    """Contain the methods to merge two arrays"""

    def __init__(self, input_array: list[int]) -> None:
        self.array = input_array

    def merge(self, array_to_merge: list[int]) -> list[int]:
        """Merge the array from init with the one passed as parameter on this method"""

        merged_array = []
        index_initial_arr = 0
        index_arr_to_merge = 0
        total_iterations = len(self.array) + len(array_to_merge)
        while index_initial_arr < len(self.array) and index_arr_to_merge < len(
            array_to_merge
        ):
            print(
                "index_initial_arr: ",
                index_initial_arr,
                " - init_array_val: ",
                self.array[index_initial_arr],
                " - index_arr_to_merge: ",
                index_arr_to_merge,
                " - merge_array_val",
                array_to_merge[index_arr_to_merge],
                " - merged_array: ",
                merged_array,
                " - total_iterations: ",
                total_iterations,
            )
            if self.array[index_initial_arr] > array_to_merge[index_arr_to_merge]:
                merged_array.append(array_to_merge[index_arr_to_merge])
                index_arr_to_merge += 1
            elif self.array[index_initial_arr] == array_to_merge[index_arr_to_merge]:
                merged_array.append(array_to_merge[index_arr_to_merge])
                merged_array.append(self.array[index_initial_arr])
                index_arr_to_merge += 1
                index_initial_arr += 1
            elif self.array[index_initial_arr] < array_to_merge[index_arr_to_merge]:
                merged_array.append(self.array[index_initial_arr])
                index_initial_arr += 1

        while index_initial_arr < len(self.array):
            merged_array.append(self.array[index_initial_arr])
            index_initial_arr += 1
        while index_arr_to_merge < len(array_to_merge):
            merged_array.append(array_to_merge[index_arr_to_merge])
            index_arr_to_merge += 1

        return merged_array
