import graphviz as gv

formats = ["svg", 'pdf', 'png', 'jpg']

nodes = ['A', 'B', 'C', 'D']

for format in formats:
    g = gv.Graph(format=format)
    for node in nodes:
        g.node(node)
    g.render('graph/demo63')