import random, time
import tabulate

def partition(arr, low, high, pivot_fn):
    pivot_index = pivot_fn(arr, low, high)
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low
    for j in range(low, high):
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def qsort(arr, low=0, high=None, pivot_fn=lambda arr, low, high: low):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high, pivot_fn)
        qsort(arr, low, pi-1, pivot_fn)
        qsort(arr, pi+1, high, pivot_fn)

def qsort_fixed_pivot(arr):
    qsort(arr, pivot_fn=lambda arr, low, high: low)

def qsort_random_pivot(arr):
    qsort(arr, pivot_fn=lambda arr, low, high: random.randint(low, high))

def time_sort(sort_fn, mylist):
    start = time.time()
    sort_fn(mylist.copy())  # Use a copy to keep the original list unchanged
    return (time.time() - start) * 1000

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    results = []
    for size in sizes:
        mylist = list(range(size))
        random_list = mylist.copy()
        random.shuffle(random_list)

        fixed_time = time_sort(qsort_fixed_pivot, random_list)
        random_time = time_sort(qsort_random_pivot, random_list)
        tim_sort_time = time_sort(sorted, random_list)
        results.append((size, fixed_time, random_time, tim_sort_time))
    return results

def print_results(results):
    print(tabulate.tabulate(results, headers=['Size', 'QSort Fixed Pivot', 'QSort Random Pivot', 'TimSort'], floatfmt=".3f", tablefmt="github"))

def test_print():
    results = compare_sort()
    print_results(results)

test_print()
