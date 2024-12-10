from common.utils import run_part
import tqdm


def p2(input: list[str]) -> int:
    int_input = [int(x) for x in input[0]]
    totalspace = sum(int_input)

    l = list(x for x in range(totalspace))

    blocks = []
    ptr = 0
    for i, instruction in enumerate(int_input):
        if i % 2 == 0:
            file_id = i // 2
            l[ptr:ptr+instruction] = [file_id] * instruction
            blocks.append((file_id, ptr, instruction))
        else:
            l[ptr:ptr+instruction] = [-1] * instruction
        ptr += instruction

    for block in tqdm.tqdm(blocks[::-1]):
        file_id, ptr, length = block
        new_index = find_block_in_array(l, length)
        if new_index == -1 or new_index >= ptr:
            continue
        l[new_index:new_index+length] = [file_id] * length
        l[ptr:ptr+length] = [-1] * length

    # Calculate checksum
    s = 0
    for i, x in enumerate(l):
        if x == -1:
            continue
        s += i * x

    return sum(i * x for i, x in enumerate(l) if x != -1)


def find_block_in_array(arr, length) -> int:
    # Returns -1 if a block of length len is not found
    for i in range(len(arr) - length):
        if arr[i:i+length] == [-1] * length:
            return i

    return -1


if __name__ == "__main__":
    run_part("09/input.txt", p2, 2)
