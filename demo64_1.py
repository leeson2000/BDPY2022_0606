import functools
import graphviz as gv
from itertools import combinations

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
g3 = graph()
g4 = digraph()


def add_nodes(g, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            pass
        else:
            g.node(n)
    return g


def add_edges(g, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            pass
        else:
            g.edge(*e)
    return g


g3_nodes = list('ABC')
g3_edges = tuple(combinations(g3_nodes, 2))
g3 = add_nodes(g3, g3_nodes)
g3 = add_edges(g3, g3_edges)
g3.render('graph/demo64')