import graphviz as gv
from itertools import combinations, permutations

formats = ["svg", 'pdf', 'png', 'jpg']

nodes = ['A', 'B', 'C', 'D']
#edges = tuple(combinations(nodes, 2))
edges = tuple(permutations(nodes, 2))
print(edges)
for format in formats:
    # g = gv.Graph(format=format)
    g = gv.Digraph(format=format)
    for node in nodes:
        g.node(node)
    for edge in edges:
        g.edge(edge[0], edge[1])
    g.render('graph/demo63')
