from common.utils import run_part
import networkx as nx


def p2(input: list[str]) -> int:
    int_input = [[int(y) for y in x] for x in input]

    G: nx.DiGraph = nx.grid_2d_graph(len(int_input), len(
        int_input[0]), periodic=False, create_using=nx.DiGraph)

    for y in range(len(int_input)):
        for x in range(len(int_input[y])):
            G.nodes[(x, y)]["height"] = int_input[y][x]

    node = G.nodes[(0, 0)]

    G_copy = G.copy()

    for node in G.nodes:
        for n in G.neighbors(node):
            if G.nodes[node]["height"] - G.nodes[n]["height"] != 1:
                G_copy.remove_edge(n, node)

    total_paths = 0
    for start in G_copy.nodes:
        if G_copy.nodes[start]["height"] != 0:
            continue
        for dest in G_copy.nodes:
            if G_copy.nodes[dest]["height"] != 9:
                continue
            paths = nx.all_simple_paths(G_copy, start, dest)
            total_paths += len([x for x in paths])

    return total_paths


if __name__ == "__main__":
    run_part("10/input.txt", p2, 2)
