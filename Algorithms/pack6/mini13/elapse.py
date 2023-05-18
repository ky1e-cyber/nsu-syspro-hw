import sys
import json
import subprocess as sp
from functools import reduce
from pathlib import Path
from typing import List
from cfg import \
    DATA_FILE_PATH, CARGO_PROJECT_PATH, N_ITERS, CARGO_PROJECT_NAME

from p_print import print_table

if __name__ == "__main__":

    data_path = Path(DATA_FILE_PATH)
    project_path = Path(CARGO_PROJECT_PATH)

    if not data_path.is_file():
        print("Data file wasn't found")
        exit(1)
        

    compilation = sp.run(
        ["cargo", "build", "--release"], 
        cwd=project_path,
    )

    if compilation.returncode != 0:
        print(
            f"Building failed, stderr:\n {compilation.stderr.decode(sys.stderr.encoding)}\n",
            file=sys.stderr,
            capture_output=True
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

    print_table(algos, results)