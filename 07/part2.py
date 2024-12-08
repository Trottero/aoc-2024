from common.utils import run_part

operator_map = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "||": lambda x, y: int(str(x) + str(y)),
}


def p2(input: list[str]) -> int:
    lines = [[int(x) for x in line.replace(":", "").split(" ")]
             for line in input]
    s = 0
    operators = ["+", "*", "||"]
    for line in lines:
        ans = line[0]
        numbers = line[2:]
        factored = factor_remaining(line[1], ans, numbers, operators)
        if factored > 0:
            s += ans

    return s


def factor_remaining(result, target, numbers, operators) -> int:
    if result == target and len(numbers) == 0:
        # Resolved
        return 1

    if result > target or len(numbers) == 0:
        # Negative too much, numbers means it cant be resolved
        return 0

    new_numbers = numbers.copy()
    next_n = new_numbers.pop(0)

    return sum(factor_remaining(operator_map[operator](
        result, next_n), target, new_numbers, operators) for operator in operators)


if __name__ == "__main__":
    run_part("07/input.txt", p2, 2)
