from typing import Any
import networkx as nx

"""Do an breadth-first search and returns list of nodes in the visited order
:param g: input graph
:param start_node: starting node for search
:return:list of nodes in the visited order """

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def bfs(g: nx.Graph, start_node: Any) -> list:
    visit, list = [], ([start_node])


    return list(g.nodes)
