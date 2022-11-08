from typing import List


def get_format_row(words: List[str], column_lens: List[int]) -> str:
    assert len(words) == len(column_lens)

    return "| " + " | ".join([f"{w:<{l}}" for w, l in zip(words, column_lens)]) + " |"


def format_table(benchmarks: List[str], algos: List[str], results: List[List[float]]):
    BENCHMARKS: str = "Benchmarks"
    results_str: List[str] = [
        list(map(lambda n: str(round(n, 2)), seq)) for seq in results]

    column_lens: List[int] = list(
        map(
            lambda xs: max(map(len, xs)),
            [[BENCHMARKS] + benchmarks] + [
                [col_name] + [
                    results_str[j][i] for j in range(len(results_str))] 
                    for i, col_name in enumerate(algos)])
    )

    print(
        "\n".join(
            [get_format_row([BENCHMARKS] + algos, column_lens),
             "|" + "-" * (sum(column_lens) + 3 * len(column_lens) - 1) + "|"] +

            [get_format_row([bench] + res, column_lens)
             for bench, res in zip(benchmarks, results_str)]
        )
    )

# surprisingly wackiest thing i have wrote thus far


if __name__ == "__main__":
    format_table(
        ["best case", "worst case"],
        ["quick sort", "merge sort", "bubble sort"],
        [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]
    )
    print()
    format_table(
        ["best case", "the worst case"],
        ["quick sort", "merge sort", "bubble sort"],
        [[1.23, 1.56, 2.0], [3.33333333, 2.9, 3.9]]
    )
