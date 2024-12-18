from common.utils import run_part
import re
import networkx as nx


def p2(input: list[str]) -> int:
    blocks = []
    for line in input:
        blocks.append(tuple(int(x) for x in re.findall(r"\d+", line)))
        pass

    maxx = max(x for x, y in blocks)
    maxy = max(y for x, y in blocks)

    G = nx.grid_2d_graph(maxx + 1, maxy + 1, create_using=nx.DiGraph)

    i = 0
    while nx.has_path(G, (0, 0), (maxx, maxy)):
        G.remove_node(blocks[i])
        i += 1

    return blocks[i-1]


if __name__ == "__main__":
    run_part("18/input.txt", p2, 2)
