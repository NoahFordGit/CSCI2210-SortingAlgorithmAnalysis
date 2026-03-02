import matplotlib.pyplot as plt
import time
from Benchmarking.dataGenerator import DataGenerator
from Sorts.radixSortString import RadixSortString

class RadixSortStringBenchmark:
    def __init__(self, filepath):
        self.filepath = filepath
        self.results = []

    def run_benchmarks(self, iterations=100):
        """
        Benchmark Radix Sort on words from a file.
        
        Args:
            iterations (int): Number of times to run the benchmark
        """
        words = DataGenerator.read_words_from_file(self.filepath)
        
        if not words:
            print("No words loaded from file.")
            return
        
        print(f"Loaded {len(words)} words from {self.filepath}")
        
        for i in range(iterations):
            # Create a copy for sorting to preserve original
            arr = words.copy()
            sorter = RadixSortString(arr)
            start = time.time()
            sorter.sort()
            elapsed = time.time() - start
            self.results.append(elapsed)
            print(f'Completed benchmark {i + 1}/{iterations}')
        
        self.plot_results()

    def plot_results(self):
        """Display benchmark results as a bar graph showing average time."""
        if not self.results:
            print("No results to plot")
            return
        
        avg_time = sum(self.results) / len(self.results)
        min_time = min(self.results)
        max_time = max(self.results)
        
        categories = ['Average', 'Min', 'Max']
        times = [avg_time, min_time, max_time]
        
        plt.bar(categories, times)
        plt.ylabel('Time (seconds)')
        plt.title(f'Radix Sort (String) Benchmark Results')
        plt.tight_layout()
        plt.show()
