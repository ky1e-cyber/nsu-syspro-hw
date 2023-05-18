import sys
import random as rng
from pathlib import Path
from typing import Iterator
from cfg import INT_MIN, INT_MAX, ARRAY_SIZE

def create_file(file_path: Path, itr: Iterator[str]):
    with open(file_path, "w") as f:
        f.write(" ".join(itr))

if __name__ == "__main__":
    from cfg import DATA_FILE_PATH

    itr: Iterator[str] = (
        (str(rng.randint(INT_MIN, INT_MAX)) for _ in range(ARRAY_SIZE))
        if (len(sys.argv) > 1 and sys.argv[1] in {"-t", "--true"}) 
        else map(str, rng.sample(range(INT_MIN, INT_MAX + 1), ARRAY_SIZE)) 
    )

    create_file(Path(DATA_FILE_PATH), itr)