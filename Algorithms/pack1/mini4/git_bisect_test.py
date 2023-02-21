import sys
from typing import Optional
import subprocess as sp
from pathlib import Path
from git_bisect import Commit

def run_check(repo_path: str, hash_start: str, hash_end: str, check_cmd: str, hash_expected: Optional[str] = None):
    ret = sp.run(
        ["python3", "git_bisect.py", repo_path, hash_start, hash_end, check_cmd], 
        capture_output=True
    )

    expect = ""

    if hash_expected is not None:
        repo_path = Path(repo_path)
        commit_exptected = Commit(hash_expected)
        commit_exptected.get_full_info(repo_path)
        expect = f"Found commit: {commit_exptected}\n"

    assert ret.returncode == 0
    assert ret.stdout.decode(sys.stdout.encoding) == expect


def test1():
    run_check(
        "./test_repo/", 
        "182af885965540c496f62331d82e34650404ddc0", 
        "38677aa1d2a398c54e230183a8c3ae68cac424a8", 
        "gcc main.c", 
        "2f544e8f7b8c15e9d36b340c9a79f0475c994696"
    )


def test2():
    run_check(
        "./test_repo/", 
        "ed8852445e34957399dc214481b70acd6bc148e7", 
        "2f544e8f7b8c15e9d36b340c9a79f0475c994696", 
        "gcc main.c", 
        "2f544e8f7b8c15e9d36b340c9a79f0475c994696"
    )


def test3():
    run_check(
        "./test_repo/", 
        "73d3d813962ed4701e41fcc8b8cec8c22f9b46b9", 
        "38677aa1d2a398c54e230183a8c3ae68cac424a8", 
        "gcc main.c", 
        "2f544e8f7b8c15e9d36b340c9a79f0475c994696"
    )

def test4():
    run_check(
        "./test_repo/", 
        "73d3d813962ed4701e41fcc8b8cec8c22f9b46b9", 
        "2f544e8f7b8c15e9d36b340c9a79f0475c994696", 
        "gcc main.c", 
        "2f544e8f7b8c15e9d36b340c9a79f0475c994696"
    )

def test5():
    run_check(
        "./test_repo/", 
        "182af885965540c496f62331d82e34650404ddc0", 
        "ad04e649b2c664232a084df4c67c19585663603e", 
        "gcc main.c"
    )