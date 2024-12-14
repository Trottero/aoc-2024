import os
from common.utils import run_part
import re
import PIL.Image as Image


def p2(input: list[str], args: tuple[int, int] = (101, 103)) -> int:
    fieldx, fieldy = args

    drones: list[int] = [
        [int(x) for x in re.findall(r"\-?\d+", line)] for line in input]

    os.makedirs("14/images", exist_ok=True)
    for _ in range(20_000):
        img = Image.new("RGB", (fieldx, fieldy), "white")
        for i, (x, y, vx, vy) in enumerate(drones):
            pos = (x, y)
            vel = (vx, vy)

            pos = step(pos, vel, (fieldx, fieldy))
            drones[i][0] = pos[0]
            drones[i][1] = pos[1]

            img.putpixel(pos, (0, 0, 0))

        img.save(f"14/images/{_}.png")

    return 0


def step(pos, vel, size) -> tuple[int, int]:
    x, y = pos
    dx, dy = vel
    x += dx
    y += dy

    maxx, maxy = size

    return (x % maxx, y % maxy)


if __name__ == "__main__":
    run_part("14/input.txt", p2, 2)
