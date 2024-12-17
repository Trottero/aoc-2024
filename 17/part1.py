from common.utils import run_part
import re


def p1(input: list[str]) -> int:
    memory = list(range(7)) + [0, 0]
    for i in range(3):
        memory[i+4] = int(re.findall(r"\d+", input[i])[0])

    operations = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv
    }

    program: list[int] = [int(x) for x in re.findall(r"\d+", input[-1])]

    stdout = []
    while memory[-2] < len(program):
        operation = program[memory[-2]]
        operand = program[memory[-2] + 1]
        memory = operations[operation](memory, operand, stdout)
        if memory[-1] == 1:
            # Just jumped, reset
            memory[-1] = 0
        else:
            memory[-2] += 2

    return ",".join(stdout)


def adv(state: list[int], operand: int, stdout: list[str]) -> list[int]:
    state[4] = int(state[4] / 2**state[operand])
    return state


def bxl(state: list[int], operand: int, stdout: list[str]) -> list[int]:
    state[5] ^= operand
    return state


def bst(state: list[int], operand: int, stdout: list[str]) -> list[int]:
    state[5] = state[operand] % 8
    return state


def jnz(state: list[int], operand: int, stdout: list[str]) -> list[int]:
    if state[4] != 0:
        state[-2] = operand  # Jump
        state[-1] = 1
    return state


def bxc(state: list[int], operand: int, stdout: list[str]) -> list[int]:
    state[5] ^= state[6]
    return state


def out(state: list[int], operand: int, stdout: list[str]) -> list[int]:
    stdout.append(str(state[operand] % 8))
    return state


def bdv(state: list[int], operand: int, stdout: list[str]) -> list[int]:
    state[5] = int(state[4] / 2**state[operand])
    return state


def cdv(state: list[int], operand: int, stdout: list[str]) -> list[int]:
    state[6] = int(state[4] / 2**state[operand])
    return state


if __name__ == "__main__":
    run_part("17/input.txt", p1, 1)
