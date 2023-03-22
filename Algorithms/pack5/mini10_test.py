import random as rng
from typing import List
from mini10 import str_radix_sort

MAX_STR_LEN = 200
MAX_SET_LEN = 100

CASES = [
    ["c", "v", "a", "b"],
    ["bca", "abc", "kkt"],
    ["caaab", "grgrg", "witle"],
    ["bcfgqer111!!231eqfefwgeq---+++++++++", "bcfgqer111!!231eqfefwgeq---++++++++=", "acfgqer111!!231eqfefwgeq---+++++++++", "bcfgqer111!!231eqfefwgeq-p-+++++++++"]
]

RANDOM_TEST_COUNT = 30

def generate_data() -> List[str]:
    l = rng.randint(1, MAX_STR_LEN)
    return [
        ("".join([chr(rng.randint(0, 127)) for _ in range(l)]))
        for _ in range(rng.randint(1, MAX_SET_LEN))
    ]

def check(strings: List[str]):
    assert str_radix_sort(strings) == sorted(strings)

def test1():
    check(CASES[0])

def test2():
    check(CASES[1])

def test3():
    check(CASES[3])

def test_random():
    for i in range(RANDOM_TEST_COUNT):
        check(generate_data())