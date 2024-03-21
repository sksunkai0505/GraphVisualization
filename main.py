import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

nodes_list = ['0', '1', '2', '3', '4',
              '5', '6', '7',# 'I', 'J',
              ]
for eachNode in nodes_list:
    G.add_node(eachNode)

edges_list = [
    ['0', '1'],
    ['1', '2'],
    ['1', '3'],
    ['1', '4'],
    ['1', '5'],
    ['2', '3'],
    ['2', '4'],
    ['3', '4'],
    ['3', '5'],
    ['4', '5'],
    ['4', '6'],
    ['6', '7'],

              # 'F', 'G', 'H',# 'I', 'J',
              ]

for eachEdge in edges_list:
    G.add_edge(eachEdge[0], eachEdge[1])


pos={
    "0": (1, 1.5),
    "1": (2, 2.5),
    "2": (2.9, 1.6),
    "3": (3.5, 3.2),
    "4": (5, 2.5),
    "5": (4.1, 1.6),
    "6": (5.7, 2),
    "7": (6.4, 1.5)
}

nx.draw(G, pos=pos,
        with_labels=True, node_color="red",
        node_size=500, font_color="white",
        font_size=20, font_family="Times New Roman",
        font_weight="bold",width=5,
        edge_color="black")
plt.margins(0.2)
plt.show()