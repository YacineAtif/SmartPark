import networkx as nx
import pandas as pd
# from graphviz import Digraph
# import pydotplus
import numpy as np


def searchPath(source, target):
    file = open('Data/Routes.txt', 'r')
    # Perform the conversion to networkx
    G_graph = nx.read_weighted_edgelist("Data/Routes.txt", delimiter=",", create_using=nx.DiGraph())

    # Find Astar path
    path = nx.astar_path(G_graph, source, target, weight='weight')
    length = nx.astar_path_length(G_graph, source, target, weight='weight')

    file.close()

    return path, length


