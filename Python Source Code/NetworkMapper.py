import networkx as nx
import pandas

G = nx.from_pandas_edgelist(df,
                            source='Source',
                            target='Target',
                            edge_attr='weight')

from pyvis.network import Network

net = Network(notebook=True)
net.from_nx(G)

net.show(example.html)