class RadixSortString:
    def __init__(self, arr):
        self.arr = arr

    def counting_sort(self, exp):
        n = len(self.arr)
        output = [0] * n
        count = [0] * 256  # Assuming ASCII character set

        for i in range(n):
            index = ord(self.arr[i][exp]) if exp < len(self.arr[i]) else 0
            count[index] += 1

        for i in range(1, 256):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = ord(self.arr[i][exp]) if exp < len(self.arr[i]) else 0
            output[count[index] - 1] = self.arr[i]
            count[index] -= 1

        for i in range(n):
            self.arr[i] = output[i]

    def radix_sort(self):
        max_length = max(len(s) for s in self.arr)
        for exp in range(max_length - 1, -1, -1):
            self.counting_sort(exp)

    def sort(self, benchmark_instance=None):
        self.radix_sort()