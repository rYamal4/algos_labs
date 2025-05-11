from typing import List

bubble_comparisons: int = 0
bubble_swaps: int = 0

bitonic_comparisons: int = 0
bitonic_swaps: int = 0

lsd_radix_comparisons: int = 0
lsd_radix_swaps: int = 0

def reset_counters() -> None:
    global bubble_comparisons, bubble_swaps
    global bitonic_comparisons, bitonic_swaps
    global lsd_radix_comparisons, lsd_radix_swaps
    bubble_comparisons = bubble_swaps = 0
    bitonic_comparisons = bitonic_swaps = 0
    lsd_radix_comparisons = lsd_radix_swaps = 0

def bubble_sort(lst: List[float]) -> List[float]:
    global bubble_comparisons, bubble_swaps
    n: int = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            bubble_comparisons += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                bubble_swaps += 1
    return lst

def bitonic_sort(lst: List[float]) -> List[float]:
    global bitonic_comparisons, bitonic_swaps
    n = len(lst)
    k = 1
    while k < n:
        k <<= 1
    padded = lst + [float('inf')] * (k - n)
    _bitonic_sort_rec(padded, 0, k, True)
    return padded[:n]

def lsd_radix_sort(arr: List[int], k: int = 1) -> List[int]:
    global lsd_radix_comparisons, lsd_radix_swaps
    if not arr:
        return arr
    max_val = max(arr)
    num_bits = max_val.bit_length()
    passes = (num_bits + k - 1) // k
    base = 1 << k
    output = arr[:]
    for i in range(passes):
        buckets: List[List[int]] = [[] for _ in range(base)]
        shift = i * k
        mask = base - 1
        for num in output:
            lsd_radix_comparisons += 1
            buckets[(num >> shift) & mask].append(num)
        tmp: List[int] = []
        for bucket in buckets:
            for num in bucket:
                tmp.append(num)
                lsd_radix_swaps += 1
        output = tmp
    return output

def _bitonic_merge(a: List[float], low: int, cnt: int, ascending: bool) -> None:
    global bitonic_comparisons, bitonic_swaps
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            bitonic_comparisons += 1
            if (a[i] > a[i + k]) == ascending:
                a[i], a[i + k] = a[i + k], a[i]
                bitonic_swaps += 1
        _bitonic_merge(a, low, k, ascending)
        _bitonic_merge(a, low + k, k, ascending)

def _bitonic_sort_rec(a: List[float], low: int, cnt: int, ascending: bool) -> None:
    if cnt > 1:
        k = cnt // 2
        _bitonic_sort_rec(a, low, k, True)
        _bitonic_sort_rec(a, low + k, k, False)
        _bitonic_merge(a, low, cnt, ascending)
