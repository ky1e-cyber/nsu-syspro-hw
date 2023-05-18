from typing import List

def get_format_row(words: List[str], column_lens: List[int]) -> str:
    assert len(words) == len(column_lens)

    return "| " + " | ".join([f"{w:<{l}}" for w, l in zip(words, column_lens)]) + " |"


def format_table(left_upp: str, rows: List[str], columns: List[str], results: List[List[float]]):
    results_str: List[str] = [
        list(map(lambda n: str(round(n, 2)), seq)) for seq in results]

    column_lens: List[int] = list(
        map(    
            lambda xs: max(map(len, xs)),
            [[left_upp] + rows] + [
                [col_name] + [
                    results_str[j][i] for j in range(len(results_str))] 
                    for i, col_name in enumerate(columns)]
        )
    )

    print(
        "\n".join(
            [get_format_row([left_upp] + columns, column_lens),
             "|" + "-" * (sum(column_lens) + 3 * len(column_lens) - 1) + "|"] +

            [get_format_row([row] + res, column_lens)
             for row, res in zip(rows, results_str)]
        )
    )

def print_table(algos, results):
    format_table("partitions", algos, ["geometric mean"], [[r] for r in results])