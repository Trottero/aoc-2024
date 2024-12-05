from common.utils import run_part
import networkx as nx


def p2(input: list[str]) -> int:
    rules = [line for line in input if "|" in line]

    manuals = [[int(x) for x in line.split(",")]
               for line in input if "|" not in line and line != ""]

    G = nx.DiGraph()
    for rule in rules:
        curr, dest = [int(x) for x in rule.split("|")]
        G.add_edge(curr, dest)

    s = 0
    for manual in manuals:
        G_manual: nx.DiGraph = G.subgraph(manual).copy()

        for entry in manual:
            if G_manual.in_degree(entry) > 0:
                break

            G_manual.remove_node(entry)

        if len(G_manual.nodes) == 0:
            continue

        # Reconstruct graph, but this time we try again :)
        G_manual = G.subgraph(manual).copy()

        order = []
        while len(G_manual.nodes) > 0:
            for node in list(G_manual.nodes):
                if G_manual.in_degree(node) == 0:
                    order.append(node)
                    G_manual.remove_node(node)

        s += order[int((len(order) - 1) / 2)]

    return s


if __name__ == "__main__":
    run_part("05/input.txt", p2, 2)
