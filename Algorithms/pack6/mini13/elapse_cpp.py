import sys, json
import subprocess as sp
from pathlib import Path
from functools import reduce
from p_print import print_table
from cfg import \
    CPP_SOURCE, CPP_EXEC, DATA_FILE_PATH, ARRAY_SIZE, N_ITERS

def unwrap(obj):
    if obj is None:
        raise ValueError("Unwrapping failed")
    return obj

data_path = Path(DATA_FILE_PATH).absolute()
src_path = Path(CPP_SOURCE).absolute()

exec_path = Path(CPP_EXEC).absolute()

clang_configs = {
    "Lomuto_standart":      ["clang++", "-std=c++17", "-O3", "-DNDEBUG", 
                             "-DLOMUTO_BRANCHY", "-o", exec_path, src_path],
    "Hoare":                ["clang++", "-std=c++17", "-O3", "-DNDEBUG", 
                             "-o", exec_path, src_path],
    "Lomuto_branchless":    ["clang++", "-std=c++17", "-O3", "-DNDEBUG", 
                             "-DLOMUTO", "-o", exec_path, src_path]
}


if not data_path.is_file():
    print("Data file wasn't found")
    exit(1)

results = dict()

for part, config in clang_configs.items():
    compilation = sp.run(
        config, 
        capture_output=True
    )

    if compilation.returncode != 0:
        print(
            f"Building failed, stderr:\n {compilation.stderr.decode(sys.stderr.encoding)}\n",
            file=sys.stderr
        )
        exit(1)
    
    elapsed_process = sp.run(
        [exec_path, data_path, str(ARRAY_SIZE), str(N_ITERS)],
        capture_output=True
    )

    if elapsed_process.returncode != 0:
        print(
            f"executable crashed, stderr:\n{elapsed_process.stderr.decode(sys.stderr.encoding)}",
            file=sys.stderr
        )
        exit(1)

    results[part] = unwrap(
        json.loads(
            elapsed_process.stdout.decode(sys.stdout.encoding)
        )
        .get("geometric_mean")
    )
    

algos, results = reduce(
    lambda prevs, nxt: (prevs[0] + [nxt[0]], prevs[1] + [nxt[1]]), 
    results.items(), 
    ([], [])
)

print_table(algos, results)