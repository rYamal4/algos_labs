from typing import List

def bubble_sort(lst: List[float]) -> List[float]:
    n: int = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def bitonic_sort(lst: List[float]) -> List[float]:
    n = len(lst)
    k = 1
    while k < n:
        k <<= 1
    padded = lst + [float('inf')] * (k - n)
    _bitonic_sort_rec(padded, 0, k, True)
    return padded[:n]

def lsd_radix_sort(arr: List[int], k: int = 1) -> List[int]:
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
            digit = (num >> shift) & mask
            buckets[digit].append(num)
        output = [num for bucket in buckets for num in bucket]
    return output

def _bitonic_merge(a: List[float], low: int, cnt: int, ascending: bool) -> None:
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            if (a[i] > a[i + k]) == ascending:
                a[i], a[i + k] = a[i + k], a[i]
        _bitonic_merge(a, low, k, ascending)
        _bitonic_merge(a, low + k, k, ascending)

def _bitonic_sort_rec(a: List[float], low: int, cnt: int, ascending: bool) -> None:
    if cnt > 1:
        k = cnt // 2
        _bitonic_sort_rec(a, low, k, True)
        _bitonic_sort_rec(a, low + k, k, False)
        _bitonic_merge(a, low, cnt, ascending)
