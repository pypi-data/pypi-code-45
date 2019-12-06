
objects = ["chaussures", "chaussettes", "slip", "pantalon",
           "ceinture", "chemise", "veste", "cravate"]
dependancies = [
    ("slip", "pantalon"),
    ("chemise", "cravate"),
    ("chemise", "pantalon"),
    ("pantalon", "ceinture"),
    ("chaussettes", "chaussures"),
    ("pantalon", "chaussures"),
    ("ceinture", "chaussures"),
    ("chemise", "veste"),
]
graph = Graph()
for o in objects:
    graph.add_node(GraphNode(o, None))
for d in dependancies:
    graph.add_link(d[0], d[1])
graph.add_node(GraphNode("subgraph", graph))

app = QtGui.QApplication.instance()
if app is None:
    app = QtGui.QApplication(sys.argv)
view = GraphView(graph)
view.show()
sys.exit(app.exec_())
