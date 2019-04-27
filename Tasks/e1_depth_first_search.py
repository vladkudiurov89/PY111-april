from typing import Any
import networkx as nx

"""Do an depth-first search and returns list of nodes in the visited order
:param g: input graph
:param start_node: starting node of search
:return: list of nodes in the visited order"""

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def dfs(g: nx.Graph, start_node: Any) -> list:
    visit, stack = [], [start_node]
    while stack:
        ziz = stack.pop()
        alfa = g.neighbors(ziz)
        if ziz not in visit:
            visit.append(ziz)
            stack. extend(set(g[ziz])-set(visit))
        # print(g, start_node)
        # return list(g.nodes)
        return visit
    print(dfs(graph, 'A'))