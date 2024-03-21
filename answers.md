# CMPS 2200 Reciation 5
## Answers

**Name:**__Raymond Liu_______________________


Place all written answers from `recitation-05.md` here for easier grading.



- **1b.**
For 1b, I examine the running times of the two Quicksort variants on lists of different characteristics. The Quicksort algorithm, with its average-case complexity of O(nlogn), demonstrates significant variability in performance depending on the choice of pivot. Using a fixed pivot, the algorithm can degrade to O(n^2) in the worst case, notably when the list is already sorted or nearly sorted, as this results in highly unbalanced partitions. In contrast, selecting a random pivot mitigates this risk, more consistently achieving its average-case performance by ensuring a greater likelihood of balanced partitions. Therefore, when comparing the running times across random and already sorted permutations, the random pivot variant is expected to exhibit more stable and generally faster performance than its fixed pivot counterpart, particularly as the size of the input list increases.



- **1c.**
For 1c, the comparison extends to include Python's sorted function. Timsort, the algorithm behind sorted, is designed to excel particularly well with partially sorted or already sorted data, taking advantage of existing order within the list to minimize the amount of work needed to sort it completely. This adaptive algorithm combines merge sort and insertion sort strategies, achieving O(nlogn) complexity in the worst case and potentially better for partially sorted input. When pitted against the fastest Quicksort variant from our previous comparison—likely the random pivot variant—Timsort is expected to show superior performance, especially as the input size grows and particularly with lists that are already or nearly sorted. The nature of Timsort's optimizations means it can outperform traditional Quicksort implementations by leveraging patterns within the data that Quicksort, with its more generalized approach, does not explicitly account for.