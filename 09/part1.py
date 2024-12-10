from common.utils import run_part


def p1(input: list[str]) -> int:
    int_input = [int(x) for x in input[0]]
    totalspace = sum(int_input)

    l = list(x for x in range(totalspace))

    ptr = 0
    for i, instruction in enumerate(int_input):
        if i % 2 == 0:
            file_id = i // 2
            l[ptr:ptr+instruction] = [file_id] * instruction
            pass
        else:
            l[ptr:ptr+instruction] = [-1] * instruction
        ptr += instruction

    ptr = len(l) - 1
    while True:
        if ptr < 0:
            break
        if l[ptr] == -1:
            ptr -= 1
            continue

        # Find the first -1 from start
        ind = l.index(-1)
        if ind > ptr:
            break

        l[ind] = l[ptr]
        l[ptr] = -1

        ptr -= 1

    # Calculate checksum
    return sum(i * x for i, x in enumerate(l) if x != -1)


if __name__ == "__main__":
    run_part("09/input.txt", p1, 1)
