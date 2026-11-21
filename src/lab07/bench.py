import csv
import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import (
    bubble_sort,
    counting_sort,
    insertion_sort,
    merge_sort,
    selection_sort,
)


def load_or_generate_numbers(n: int, lo: int = -100_000, hi: int = 100_000) -> list[int]:
    """Читает сэмпл из data/samples/lab07/numbers_{n}.csv, если он есть,
    иначе генерирует детерминированный список из n элементов.
    """
    sample_path = Path(f"data/samples/lab07/numbers_{n}.csv")
    if sample_path.exists():
        with sample_path.open(encoding="utf-8") as f:
            return [int(row["value"]) for row in csv.DictReader(f)]
    return [random.randint(lo, hi) for _ in range(n)]


def bench_sorts() -> list[tuple[str, int, str, str]]:
    """Бенчмарк сортировок на n = 1_000, 10_000, 100_000."""
    rows: list[tuple[str, int, str, str]] = []
    sizes = [1_000, 10_000, 100_000]

    for n in sizes:
        data = load_or_generate_numbers(n)
        lo_val, hi_val = min(data), max(data)

        # Встроенный sorted (Timsort)
        t = timeit.timeit(lambda: sorted(data), number=1)
        rows.append(("sort", n, "sorted", f"{t:.6f}"))

        # (★) Итеративный merge_sort — O(n log n)
        t = timeit.timeit(lambda: merge_sort(data), number=1)
        rows.append(("sort", n, "merge_sort", f"{t:.6f}"))

        # (★) Counting sort — O(n + k)
        t = timeit.timeit(lambda: counting_sort(data, lo_val, hi_val), number=1)
        rows.append(("sort", n, "counting_sort", f"{t:.6f}"))

        # Квадратичные сортировки: на 100_000 работают десятки минут -> ставим "> 60"
        for name, fn in (
            ("bubble_sort", bubble_sort),
            ("insertion_sort", insertion_sort),
            ("selection_sort", selection_sort),
        ):
            if n >= 100_000:
                rows.append(("sort", n, name, "> 60"))
            else:
                t = timeit.timeit(lambda: fn(data), number=1)
                rows.append(("sort", n, name, f"{t:.6f}"))

    return rows


def bench_search() -> list[tuple[str, int, str, str]]:
    """Бенчмарк поиска: 10 000 случайных запросов к списку из 100 000 элементов."""
    rows: list[tuple[str, int, str, str]] = []
    n = 100_000
    queries_count = 10_000

    data = load_or_generate_numbers(n)
    # Половина запросов — реально существующие элементы, половина — случайные
    queries = [
        random.choice(data) if i % 2 == 0 else random.randint(-150_000, 150_000)
        for i in range(queries_count)
    ]

    # Линейный поиск (10 000 запросов)
    t_lin = timeit.timeit(
        lambda: [linear_search(data, q) for q in queries],
        number=1,
    )
    rows.append(("search_10k", n, "linear_search", f"{t_lin:.6f}"))

    # Сортировка перед бинарным поиском (отдельной строкой по ТЗ)
    t_prep = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("search_10k", n, "pre_sort_for_binary", f"{t_prep:.6f}"))

    sorted_data = sorted(data)
    # Бинарный поиск (10 000 запросов на уже отсортированном списке)
    t_bin = timeit.timeit(
        lambda: [binary_search(sorted_data, q) for q in queries],
        number=1,
    )
    rows.append(("search_10k", n, "binary_search", f"{t_bin:.6f}"))

    return rows


def bench_two_sum() -> list[tuple[str, int, str, str]]:
    """Бенчмарк Two Sum на n = 1_000 и 10_000 (target гарантированно существует)."""
    rows: list[tuple[str, int, str, str]] = []
    for n in (1_000, 10_000):
        data = load_or_generate_numbers(n)
        # Гарантируем наличие ответа в самом конце списка (худший случай для brute)
        i, j = n - 2, n - 1
        target = data[i] + data[j]

        t_brute = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_brute", f"{t_brute:.6f}"))

        t_fast = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_fast", f"{t_fast:.6f}"))

    return rows


def plot_sort_benchmark(rows: list[tuple[str, int, str, str]], out_path: str) -> None:
    """(★) Строит график времени сортировок от n с логарифмической осью Y."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Предупреждение: matplotlib не установлен, график пропущен.")
        return

    series: dict[str, tuple[list[int], list[float]]] = {}
    for task, n, impl, sec_str in rows:
        if task != "sort" or sec_str.startswith(">"):
            continue
        series.setdefault(impl, ([], []))
        series[impl][0].append(n)
        series[impl][1].append(float(sec_str))

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(9, 5))
    for impl, (xs, ys) in series.items():
        plt.plot(xs, ys, marker="o", linewidth=2, label=impl)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Размер массива n (лог. шкала)")
    plt.ylabel("Время выполнения, с (лог. шкала)")
    plt.title("Сравнение времени сортировок (ЛР7)")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()


def main() -> None:
    random.seed(42)
    all_rows: list[tuple[str, int, str, str]] = []
    all_rows.extend(bench_sorts())
    all_rows.extend(bench_search())
    all_rows.extend(bench_two_sum())

    # Вывод выровненной таблицы в консоль
    header = ("task", "n", "impl", "seconds")
    print(f"{header[0]:<12} | {header[1]:>8} | {header[2]:<20} | {header[3]:>10}")
    print("-" * 59)
    for task, n, impl, sec in all_rows:
        print(f"{task:<12} | {n:>8} | {impl:<20} | {sec:>10}")

    # Сохранение в CSV через write_csv из ЛР4
    out_csv = Path("data/lab07/bench.csv")
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    write_csv(all_rows, out_csv, header=header)

    # (★) Построение графика
    plot_sort_benchmark(all_rows, "images/lab07/sorts_bench.png")


if __name__ == "__main__":
    main()