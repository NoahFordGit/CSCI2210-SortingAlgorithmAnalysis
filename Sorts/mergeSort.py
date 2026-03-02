class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self._merge_sort(arr[:mid])
        right_half = self._merge_sort(arr[mid:])

        return self.merge(left_half, right_half)

    def sort(self, benchmark_instance=None):
        # perform in-place merge sort on self.arr
        self.arr[:] = self._merge_sort(self.arr)