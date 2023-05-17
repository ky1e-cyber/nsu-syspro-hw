import random as rng
from pathlib import Path
from cfg import INT_MIN, INT_MAX, ARRAY_SIZE

def generate_file(file_path: Path):
    with open(file_path, "w") as f:
        f.write(" ".join(
                map(
                    str, 
                    rng.sample(range(INT_MIN, INT_MAX + 1), ARRAY_SIZE)
                )
            ))

if __name__ == "__main__":
    from cfg import DATA_FILE_PATH
    generate_file(Path(DATA_FILE_PATH))