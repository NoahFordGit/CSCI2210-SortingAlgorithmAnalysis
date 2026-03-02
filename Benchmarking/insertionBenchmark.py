import matplotlib.pyplot as plt
import time
from Benchmarking.dataGenerator import DataGenerator
from Sorts.insertionSort import InsertionSort

class InsertionBenchmark:
    def __init__ (self):
        self.results = {
            'sorted1000': [],
            'random1000': [],
            'reverse1000': [],
            'sorted100000': [],
            'random100000': [],
            'reverse100000': []
        }

    def run_benchmarks(self):

        # Benchmark sorted 1000 array
        arr = DataGenerator.generate_sorted_1000()
        sorter = InsertionSort(arr)
        start = time.time()
        sorter.sort()
        elapsed = time.time() - start
        self.results['sorted1000'].append(elapsed)

        # Benchmark sorted 100000 array
        arr = DataGenerator.generate_sorted_100000()
        sorter = InsertionSort(arr)
        start = time.time()
        sorter.sort()
        elapsed = time.time() - start
        self.results['sorted100000'].append(elapsed)
        print('Completed sorted 100000 benchmark')

        # Benchmark reverse 1000 array
        arr = DataGenerator.generate_reverse_1000()
        sorter = InsertionSort(arr)
        start = time.time()
        sorter.sort()
        elapsed = time.time() - start
        self.results['reverse1000'].append(elapsed)
        print('Completed reverse 1000 benchmark')

        # Benchmark reverse 100000 array
        arr = DataGenerator.generate_reverse_100000()
        sorter = InsertionSort(arr)
        start = time.time()
        sorter.sort()
        elapsed = time.time() - start
        self.results['reverse100000'].append(elapsed)
        print('Completed reverse 100000 benchmark')

        for i in range(100):
            # Benchmark random 1000array
            arr = DataGenerator.generate_random_1000()
            sorter = InsertionSort(arr)
            start = time.time()
            sorter.sort()
            elapsed = time.time() - start
            self.results['random1000'].append(elapsed)
            print(f'Completed random 1000 benchmark {i + 1}/100')

        for i in range(100):
            # Benchmark random 100000 array
            arr = DataGenerator.generate_random_100000()
            sorter = InsertionSort(arr)
            start = time.time()
            sorter.sort()
            elapsed = time.time() - start
            self.results['random100000'].append(elapsed)
            print(f'Completed random 100000 benchmark {i + 1}/100')

        self.plot_results()

    def plot_results(self):
        labels = ['sorted 1000', 'random 1000', 'reverse 1000', 'sorted 100,000', 'random 100,000', 'reverse 100,000']
        data = [self.results['sorted1000'], 
                self.results['random1000'], 
                self.results['reverse1000'], 
                self.results['sorted100000'], 
                self.results['random100000'], 
                self.results['reverse100000']]
        
        # Calculate average time for each category
        averages = [sum(times) / len(times) if times else 0 for times in data]

        plt.bar(range(len(averages)), averages, tick_label=labels)
        plt.xlabel('Array Type')
        plt.ylabel('Average Time (seconds)')
        plt.title('Insertion Sort Benchmark Results')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
