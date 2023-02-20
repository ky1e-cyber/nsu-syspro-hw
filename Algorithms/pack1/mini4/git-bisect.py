#!/usr/bin/env python3

from typing import List, Tuple, Optional
from collections import UserList
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
import subprocess as sp
import sys


class ResultType(Enum):
    Ok = True
    Err = False

Result = lambda t: Tuple[ResultType, Optional[t]]

@dataclass(frozen=True)
class Commit:
    commit_hash: str
    msg: Optional[str] = None
    author: Optional[str] = None
    _hash: Optional[int] = None 

    def __str__(self) -> str:
        return (
            f"Commit {self.commit_hash}" 
            + (f"\nAuthor: {self.author}" if not self.author is None else "") 
            + (f"\nMessage: {self.msg}" if not self.msg is None else "")
        )

    def __hash__(self) -> int:
        if not self._hash:
            self._hash = int(self.commit_hash, base=16)
        return self._hash

    def get_full_info(self, cwd: Path) -> Result(None):
        res = sp.run(["git", "show", "-s", "--format=%an%n%s", self.commit_hash], capture_output=True, cwd=cwd)
        if res.returncode == 0:
            self.author, self.msg = (
                res
                .stdout
                .decode(sys.stdout.encoding)
                .splitlines()
            ) 

            return ResultType.Ok, None
        
        return ResultType.Err, None

class CommitsList(UserList[Commit]):
    def get_range(self, hash_start: str, hash_end: str) -> UserList[Commit]:
        start_ind = 0
        end_ind = 0

        for i, commit in enumerate(self):
            if commit.commit_hash == hash_start:
                start_ind = i
            elif commit.commit_hash == hash_end:
                end_ind = i

        return self[start_ind:end_ind + 1:]



def get_full_hash(short_hash: str, cwd: Path) -> Optional[str]:
    ret = sp.run(
        ["git", "rev-parse", short_hash], 
        capture_output=True, 
        cwd=cwd
    )

    return (
        ret.stdout.decode(sys.stdout.encoding)[:-1:] 
        if ret.returncode != 0 else None
    )


def parse_log(repo_dir: Path) -> Result(CommitsList):

    ret = sp.run(
        ["git", "log", "--format=%H", "--no-merges"],
        capture_output=True, 
        cwd=repo_dir
    ) 

    return (
        (ResultType.Err, None) if ret.returncode != 0     
        else (
            ResultType.Ok, CommitsList(
                Commit(commit_hash) 
                for commit_hash 
                in (ret.stdout
                    .decode(sys.stdout.encoding)
                    .splitlines())
            )
        )
    )

def run_check(check_cmd: List[str], cwd: Path, commit_hash: str) -> Result(int):
    checkout_ret_code: int = (
        sp.run(
            ["git", "checkout", commit_hash], 
            cwd=cwd, stdout=sp.DEVNULL
        )
        .returncode
    )

    if checkout_ret_code != 0:
        return ResultType.Err, None
    
    return ResultType.Ok, (
        sp.run(
            cmd, 
            cwd=cwd, 
            stdout=sp.DEVNULL
        )
        .returncode
    )

def bisect(commits: CommitsList, cwd: Path, cmd: List[str]) -> Optional[Commit]:
    if len(commits) <= 0:
        return None
    
    good_bound = -1
    bad_bound = len(commits)

    while bad_bound < (good_bound + 1):
        pivot = (good_bound + bad_bound) // 2
        res, exit_code = run_check(cmd, cwd, commits[pivot].commit_hash)

        if not res:
            return None

        if exit_code == 0:
            good_bound = pivot
        else:
            bad_bound = pivot

    return commits[bad_bound] if bad_bound < len(commits) else None

ARGV = sys.argv

USAGE = (f"Usage: {ARGV[0]}" 
        " [Repository path]" 
        " [Commmit hash start]" 
        " [Commmit hash end] [Check command]"
        )

def exit_script(msg: str, to_commit: Commit):
    pass

if __name__ == "__main__":
    assert len(ARGV) == 5, "\n" + USAGE

    repo_path, hash_start, hash_end, cmd = ARGV[1::]

    repo_path = Path(repo_path)


    hash_start, hash_end = map(
        lambda h: 
            get_full_hash(h, repo_path) if len(h) < 40 else h, 
            (hash_start, hash_end)
    )

    res_code, commits = parse_log(repo_path)

    if res_code == ResultType.Err:
        print("Cannot parse commits log", file=sys.stderr)
        exit(1)

    commits = commits.get_range(hash_start, hash_end)
    cmd = cmd.split()

    current_commit = Commit(
        (sp.run(
            ["git", "show", "-s", "--format=%H"], 
            cwd=repo_path, 
            capture_output=True
        )
        .stdout
        .decode(sys.stdout.encoding)[:-1:])
    )

    bad_commit = bisect(commits, repo_path, cmd)
    if bad_commit:
        bad_commit.get_full_info(repo_path)
        print(f"Found commit: {bad_commit}")

    checkout_res = sp.run(
        ["git", "checkout", current_commit.commit_hash],
        capture_output=True,
        cwd=repo_path
    )

    if checkout_res.returncode != 0:
        print(
            f"ERROR: Can't return back to commit {current_commit.commit_hash}:\n{checkout_res.stderr.decode(sys.stderr.encoding)}", 
            file=sys.stderr
        )

    exit(checkout_res.returncode)