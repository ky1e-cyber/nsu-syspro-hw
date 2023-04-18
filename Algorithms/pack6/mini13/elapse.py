import sys
import json
import subprocess as sp
from functools import reduce
from pathlib import Path
from typing import List
from cfg import \
    DATA_FILE_PATH, CARGO_PROJECT_PATH, N_ITERS, CARGO_PROJECT_NAME

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

data_path = Path(DATA_FILE_PATH)
project_path = Path(CARGO_PROJECT_PATH)

if not data_path.is_file():
    print("Data file wasn't found, generating..")
    from generate_data import generate_file
    generate_file(data_path)

compilation = sp.run(
    ["cargo", "build", "--release"], 
    cwd=project_path, 
    capture_output=True
)

if compilation.returncode != 0:
    print(
        f"Building failed, stderr:\n {compilation.stderr.decode(sys.stderr.encoding)}\n",
        file=sys.stderr
    )
    exit(1)

exec_path = (((project_path / 
               "target")    / 
               "release")   / 
               CARGO_PROJECT_NAME)

elapsed_process = sp.run(
    [exec_path.absolute(), data_path.absolute(), str(N_ITERS)], 
    capture_output=True
)

if elapsed_process.returncode != 0:
    print(
        f"executable crashed, stderr:\n{elapsed_process.stderr.decode(sys.stderr.encoding)}", 
        file=sys.stderr
    )
    exit(0)


print(
    elapsed_process
        .stdout
        .decode(sys.stdout.encoding)
)


json_table = json.loads(
    elapsed_process
        .stdout
        .decode(sys.stdout.encoding)
)

algos, results = reduce(
    lambda prevs, nxt: (prevs[0] + [nxt[0]], prevs[1] + [nxt[1]]), 
    json_table.items(), 
    ([], [])
)

format_table("partitions", algos, ["geometric mean"], [[r] for r in results])
