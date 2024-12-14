from common.utils import run_part
import networkx as nx
from itertools import combinations


def p2(input: list[str]) -> int:
    G: nx.Graph = nx.grid_2d_graph(
        len(input[0]) + 2, len(input) + 2, periodic=False)

    ymax = len(input) + 2
    xmax = len(input[0]) + 2
    for x in range(len(input[0]) + 2):
        G.nodes[(x, 0)]['plot'] = '0'
        G.nodes[(x, ymax - 1)]['plot'] = '0'

    for y in range(len(input) + 2):
        G.nodes[(0, y)]['plot'] = '0'
        G.nodes[(xmax - 1, y)]['plot'] = '0'

    for y, line in enumerate(input):
        for x, val in enumerate(line):
            G.nodes[(x + 1, y + 1)]['plot'] = val

    G_fences = G.copy()
    G_plots = G.copy()

    for source, dest in G.edges:
        if G.nodes[source]['plot'] == G.nodes[dest]['plot']:
            G_fences.remove_edge(source, dest)
        else:
            G_plots.remove_edge(source, dest)

    s = 0
    for component in nx.connected_components(G_plots):
        if any(G.nodes[x]['plot'] == '0' for x in component):
            continue

        nodes_with_2_adjecent_fences = [
            x for x in component if G_fences.degree(x) >= 2]
        outer_corners = 0
        for node in nodes_with_2_adjecent_fences:
            neighbors = list(G_fences.neighbors(node))
            # Generate all combinations of neighbors
            for (n1, n2) in combinations(neighbors, 2):
                # Check if the neighbors share any same node
                if any(n2neigh in G.neighbors(n1) for n2neigh in G.neighbors(n2) if n2neigh != node):
                    outer_corners += 1

        # Inner corners are corners with atleast 2 adjacent plots, and these adjecent plots need to share the same neighbor
        nodes_with_2_adjacent_plots = [
            x for x in component if G_plots.degree(x) >= 2]
        inner_corners = 0
        for node in nodes_with_2_adjacent_plots:
            neighbors = list(G_plots.neighbors(node))
            # Generate all combinations of neighbors
            for (n1, n2) in combinations(neighbors, 2):
                # Check if the neighbors share any fence
                if any(G_fences.has_edge(n1, neighboring_fence) and G_fences.has_edge(n2, neighboring_fence) for neighboring_fence in G_fences.neighbors(n1)):
                    inner_corners += 1

        letter = G.nodes[next(iter(component))]['plot']
        area = len(component)
        cost = (outer_corners + inner_corners) * area

        s += cost

    return s


if __name__ == "__main__":
    run_part("12/input.txt", p2, 2)
