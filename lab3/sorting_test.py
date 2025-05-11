import time
import random
from typing import List, Callable

from lab3 import sorting_algorithms as sa
import list_generators as lg

SEED = 319

def check_sorting_algorithm(
    gen_function: Callable[[random.Random, int], List[float]],
    sort_function: Callable[[List[float]], List[float]],
    count: int
) -> float:
    rng = random.Random(SEED)
    data = gen_function(rng, count)
    start = time.perf_counter()
    sort_function(data.copy())
    return time.perf_counter() - start

if __name__ == "__main__":
    N = 5000
    bubble_time = check_sorting_algorithm(lg.random_list, sa.bubble_sort, N)
    print(
        f"Сортировка пузырьком (N = {N}): сравнений = {sa.bubble_comparisons}, замен = {sa.bubble_swaps}, time={bubble_time:.6f}s"
    )

    bitonic_time = check_sorting_algorithm(lg.random_list, sa.bitonic_sort, N)
    print(
        f"Битонная сортировка (N = {N}): сравнений = {sa.bitonic_comparisons}, замен = {sa.bitonic_swaps}, time={bitonic_time:.6f}s"
    )

    radix_time = check_sorting_algorithm(lg.random_list, sa.lsd_radix_sort, N)
    print(
        f"Lsd сортировка (N = {N}): сравнений = {sa.lsd_radix_comparisons}, замен = {sa.lsd_radix_swaps}, time={radix_time:.6f}s"
    )

    print("\n")

    sorting_algos = {
        sa.bubble_sort: "сортировка пузырьком",
        sa.bitonic_sort: "битонная сортировка",
        sa.lsd_radix_sort: "lsd сортировка"
    }
    list_generators = {
        lg.random_list: "массив случайных чисел",
        lg.random_list_with_repeats: "массив случайных чисел с большим количеством повторений одного элемента",
        lg.almost_sorted_list: "массив из отсортированных подмассивов",
        lg.sorted_subarrays_list: "отсортированный массив, в котором процент чисел заменены на случайные"
    }
    list_sizes = [100, 1_000, 10_000]

    for gen_func, gen_name in list_generators.items():
        for sort_func, sort_name in sorting_algos.items():
            for n in list_sizes:
                sa.reset_counters()
                elapsed = check_sorting_algorithm(gen_func, sort_func, n)
                print(
                    f"{gen_name}, алгоритм: {sort_name}, N = {n}, "
                    f"time={elapsed:.6f}s"
                )
