from typing import List

def parse_matrix(s: str) -> List[List[float]]:
    return [[float(x) for x in line.split()] for line in input().split("|")]


if __name__ == "__main__":
    inp = input()
    print(parse_matrix(inp))