
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
            g.node(n[0], **n[1])
        else:
            g.node(n)
    return g


def add_edges(g, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            g.edge(*e[0], **e[1])
        else:
            g.edge(*e)
    return g


g3_nodes = list('ABC')
g3_edges = tuple(combinations(g3_nodes, 2))
g3 = add_nodes(g3, g3_nodes)
g3 = add_edges(g3, g3_edges)
g3.render('graph/demo64')

node1 = ('A', {'label': "Node A"})
node2 = ('B', {'label': "Node B"})
node3 = ('C', {'label': '某個節點'})
node4 = ('D', {})
g5_nodes = [node1, node2, node3, node4]
e1 = (('A', 'B'), {'label': 'edge1'})
e2 = (('A', 'C'), {'label': 'Edge 2'})
e3 = (('B', 'C'), {'label': '某種關聯'})
e4 = (('B', 'D'), {})
g5_edges = [e1, e2, e3, e4]
g5 = digraph()
g5 = add_nodes(g5, g5_nodes)
g5 = add_edges(g5, g5_edges)
g5.render('graph/demo64_g5')


def apply_styles(g, styles):
    g.graph_attr.update('graph' in styles and styles['graph'] or {})
    return g


styles = {'graph': {'label': 'graphviz生成',
                    'fontsize': '24',
                    'fontcolor': '#ff8800',
                    'bgcolor': '#C0FFEE',
                    'rankdir': 'TB',
                    'fillcolor': '#FF0000'}}
g6 = apply_styles(g5, styles)
g6.render('graph/demo64_g6')