from common.utils import run_part
import networkx as nx


def p1(input: list[str]) -> int:
    G: nx.Graph = nx.grid_2d_graph(len(input[0]) + 2, len(input) + 2, periodic=False)

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
        s += len(component) * sum(deg for _, deg in G_fences.degree(component))

    return s


if __name__ == "__main__":
    run_part("12/input.txt", p1, 1)
