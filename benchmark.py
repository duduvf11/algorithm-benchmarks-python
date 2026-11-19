from time import perf_counter
import random

sizes = [1000, 10000, 30000]
datasets = {}

for n in sizes:
    random_data = [random.randint(0, 100000) for _ in range(n)]
    sorted_data = sorted(random_data)
    inverted_data = sorted(random_data, reverse=True)

    datasets[n] = {
        "random": random_data,
        "sorted": sorted_data,
        "inverted": inverted_data,
    }


def search_minor(arr):
    minor = arr[0]
    minor_index = 0
    for i in range(1, len(arr)):
        if arr[i] < minor:
            minor = arr[i]
            minor_index = i
    return minor_index


def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        minor_index = search_minor(arr)
        new_arr.append(arr.pop(minor_index))
    return new_arr


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = random.choice(arr)
    smaller = [i for i in arr if i < pivot]
    equal = [i for i in arr if i == pivot]
    bigger = [i for i in arr if i > pivot]
    return quick_sort(smaller) + equal + quick_sort(bigger)


print(f"{'Tamanho':<10} | {'Tipo':<10} | {'Selection (s)':<15} | {'Quicksort (s)':<15}")
print("-" * 58)

for n in sizes:
    for kind in ["random", "sorted", "inverted"]:
        data = datasets[n][kind]

        start = perf_counter()
        selection_sort(data.copy())
        sel_time = perf_counter() - start

        start = perf_counter()
        quick_sort(data.copy())
        quick_time = perf_counter() - start

        print(f"{n:<10} | {kind:<10} | {sel_time:<15.5f} | {quick_time:<15.5f}")