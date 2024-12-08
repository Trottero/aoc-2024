from common.utils import run_part


operator_map = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def p1(input: list[str]) -> int:
    lines = [[int(x) for x in line.replace(":", "").split(" ")]
             for line in input]
    s = 0
    operators = ["-", "/"]
    for line in lines:
        ans = line[0]
        numbers = line[1:][::-1]
        factored = factor_remaining(ans, numbers, operators)
        if factored > 0:
            s += ans

    return s


def factor_remaining(result, numbers, operators) -> int:
    if result == 0 and len(numbers) == 0:
        # Resolved
        return 1

    if result < 0 or len(numbers) == 0:
        # Negative too much, numbers means it cant be resolved
        return 0

    new_numbers = numbers.copy()
    next_n = new_numbers.pop(0)
    return sum(factor_remaining(operator_map[operator](result, next_n), new_numbers, operators) for operator in operators)


if __name__ == "__main__":
    run_part("07/input.txt", p1, 1)
