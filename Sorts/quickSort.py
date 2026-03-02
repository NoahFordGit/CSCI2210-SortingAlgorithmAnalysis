class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def quick_sort(self, low, high):
        # use tail recursion elimination to prevent stack overflow
        while low < high:
            pi = self.partition(low, high)
            # recurse on smaller partition first
            if pi - low < high - pi:
                self.quick_sort(low, pi - 1)
                low = pi + 1
            else:
                self.quick_sort(pi + 1, high)
                high = pi - 1

    def sort(self, benchmark_instance=None):
        # perform quick sort on the internal array
        self.quick_sort(0, len(self.arr) - 1)