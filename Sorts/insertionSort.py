class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self, benchmark_instance=None):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
