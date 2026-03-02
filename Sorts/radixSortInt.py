class RadixSortInt:
    def __init__(self, arr):
        self.arr = arr

    def counting_sort(self, exp):
        n = len(self.arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (self.arr[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = (self.arr[i] // exp) % 10
            output[count[index] - 1] = self.arr[i]
            count[index] -= 1

        for i in range(n):
            self.arr[i] = output[i]

    def radix_sort(self):
        max_num = max(self.arr)
        exp = 1
        while max_num // exp > 0:
            self.counting_sort(exp)
            exp *= 10

    def sort(self, benchmark_instance=None):
        self.radix_sort()