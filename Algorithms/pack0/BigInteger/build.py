#!/usr/bin/env python3

from typing import List, TextIO
import subprocess as sp
import random as rng
import sys, os

def run_test(cmd: List[str], operand1: int, operand2: int, log_file: TextIO):
    res = sp.run(cmd + [str(operand1), str(operand2)], capture_output=True)

    div_expect, mul_expect = operand1 // operand2, operand1 * operand2 

    div_res, mul_res = map(
        int, 
        res.stdout.decode().split()
    )

    if (div_expect, mul_expect) != (div_res, mul_res):
        s = (
                f"failed with operands: {operand1} {operand2}\n"
                + f"expected result: {div_expect} {mul_expect}\n"
                + f"got: {div_res} {mul_res}"
            )

        print(s)
        print(s, file=log_file)

if __name__ == "__main__":

    INPUT_NAME = "./Main.kt"
    OUTPUT_NAME = "./build/Main.jar"
    LOG_FILE_NAME = "./test_log.txt"
    CMD = ["java", "-jar", OUTPUT_NAME]
    MAX_INT = 4 * sys.maxsize
    TEST_COUNT = 1024

    ## Compile
    sp.run(["kotlinc", INPUT_NAME, "-include-runtime", "-d", OUTPUT_NAME])

    os.remove(LOG_FILE_NAME)

    with open(LOG_FILE_NAME, "w") as log_file:
        ## Special cases
        print("running special cases tests..")
        run_test(CMD, 0, MAX_INT, log_file)
        run_test(CMD, MAX_INT, 1, log_file)
        run_test(CMD, MAX_INT, MAX_INT, log_file)

        ## Randomize tests
        for n in range(TEST_COUNT):
            print(f"running test {n + 1}/{TEST_COUNT}..")
            run_test(CMD, rng.randint(0, MAX_INT), rng.randint(1, MAX_INT), log_file)
            