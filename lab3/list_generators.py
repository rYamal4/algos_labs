import random
from typing import List

K = 0.20
L = 12
M = 0.04
MIN_VALUE = -9999999
MAX_VALUE = 9999999

def random_list(rng: random.Random, n: int) -> List[int]:
    return [rng.randint(MIN_VALUE, MAX_VALUE) for _ in range(n)]

def random_list_with_repeats(rng: random.Random, n: int) -> List[int]:
    count_repeat = int(n * K)
    repeat_value = rng.randint(MIN_VALUE, MAX_VALUE)
    rest = [rng.randint(MIN_VALUE, MAX_VALUE) for _ in range(n - count_repeat)]
    lst = [repeat_value] * count_repeat + rest
    rng.shuffle(lst)
    return lst

def sorted_subarrays_list(rng: random.Random, n: int) -> List[int]:
    base = n // L
    extra = n % L
    lst: List[int] = []
    for i in range(L):
        size = base + (1 if i < extra else 0)
        sub = [rng.randint(MIN_VALUE, MAX_VALUE) for _ in range(size)]
        sub.sort()
        lst.extend(sub)
    return lst

def almost_sorted_list(rng: random.Random, n: int) -> List[int]:
    lst = sorted(rng.randint(MIN_VALUE, MAX_VALUE) for _ in range(n))
    count_replace = int(n * M)
    indices = rng.sample(range(n), count_replace)
    for i in indices:
        lst[i] = rng.randint(MIN_VALUE, MAX_VALUE)
    return lst
