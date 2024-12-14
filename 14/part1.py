from common.utils import run_part
import re


def p1(input: list[str], args: tuple[int, int] = (101, 103)) -> int:
    fieldx, fieldy = args

    drones: list[int] = [
        [int(x) for x in re.findall(r"\-?\d+", line)] for line in input]

    periods: list[int] = []
    for drone in drones:
        x, y, vx, vy = drone
        visited = set([(x, y)])
        pos = (x, y)
        vel = (vx, vy)
        period = 0
        while True:
            pos = step(pos, vel, (fieldx, fieldy))
            period += 1
            if pos in visited:
                break
            visited.add(pos)

        periods.append(period)

    minutes = 100

    drone_positions = []
    for i, (x, y, vx, vy) in enumerate(drones):
        pos = (x, y)
        vel = (vx, vy)

        remainder = minutes
        remainder = minutes % periods[i]

        for _ in range(remainder):
            pos = step(pos, vel, (fieldx, fieldy))

        drone_positions.append(pos)

    q1 = q2 = q3 = q4 = 0
    for (x, y) in drone_positions:
        print(f"{x}, {y}")
        if x < fieldx // 2 and y < fieldy // 2:
            q1 += 1
        elif x >= (fieldx + 1) // 2 and y < fieldy // 2:
            q2 += 1
        elif x < fieldx // 2 and y >= (fieldy + 1) // 2:
            q3 += 1
        elif x >= (fieldx + 1) // 2 and y >= (fieldy + 1) // 2:
            q4 += 1

    for y in range(fieldy):
        for x in range(fieldx):
            if (x, y) in drone_positions:
                print("#", end="")
            else:
                print(".", end="")
        print()

    return q1 * q2 * q3 * q4


def step(pos, vel, size) -> tuple[int, int]:
    x, y = pos
    dx, dy = vel
    x += dx
    y += dy

    maxx, maxy = size

    return (x % maxx, y % maxy)


if __name__ == "__main__":
    run_part("14/input.txt", p1, 1)
