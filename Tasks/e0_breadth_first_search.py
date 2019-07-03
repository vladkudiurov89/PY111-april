from typing import Any
import networkx as nx


def bfs(g: nx.Graph, start_node: Any) -> list:
    """Do an breadth-first search and returns list of nodes in the visited order
    :param g: input graph
    :param start_node: starting node for search
    :return:list of nodes in the visited order """
    visit, queue = [], ([start_node])
    while queue:
        way = queue.pop(0)
        if way not in visit:
            visit.append(way)
            queue.extend(list(g[way]))
    return visit


