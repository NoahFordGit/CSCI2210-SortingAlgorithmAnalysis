from Benchmarking import insertionBenchmark, mergeSortBenchmark, quickSortBenchmark, radixSortIntBenchmark
from Benchmarking.radixSortStringBenchmark import RadixSortStringBenchmark

insertionBenchmark = insertionBenchmark.InsertionBenchmark()
insertionBenchmark.run_benchmarks()

mergeSortBenchmark = mergeSortBenchmark.MergeSortBenchmark()
mergeSortBenchmark.run_benchmarks()

quickSortBenchmark = quickSortBenchmark.QuickSortBenchmark()
quickSortBenchmark.run_benchmarks()

radixSortIntBenchmark = radixSortIntBenchmark.RadixSortIntBenchmark()
radixSortIntBenchmark.run_benchmarks()

radixSortStringBenchmark = RadixSortStringBenchmark('words.txt')
radixSortStringBenchmark.run_benchmarks()