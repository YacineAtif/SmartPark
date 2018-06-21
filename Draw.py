import pandas as pd
import numpy as np
import networkx as nx
from graphviz import Digraph
import matplotlib.pyplot as plt


def DrawFromPanda(file):
    G_map = Digraph(format='jpeg')
    G_map.attr(rankdir='LR', size='8,5')
    G_map.attr('node', shape='circle')

    df = pd.read_csv(file, sep=",", header=None, engine='python')

    nodelist = []
    for idx, row in df.iterrows():
        node1, node2, weight = [str(i) for i in row]

        if node1 not in nodelist:
            G_map.node(node1)
            nodelist.append(node2)

        if node2 not in nodelist:
            G_map.node(node2)
            nodelist.append(node2)

        G_map.edge(node1, node2, label=weight)

    G_map.render('Output/graph', view=True)

    return G_map


def showRoutes():
    file = open('Data/Routes.txt', 'r')
    G_map = DrawFromPanda(file)
    file.close()


def drawMarkovChain(states):

    # create state space and initial state probabilities

    #pi = [0.2, 0.2, 0.2,0.2,0.1,0.1]

    #  create transition matrix
    #  equals transition probability matrix of changing states given a state
    #  matrix is size (M x M) where M is number of states

    q_df = pd.read_csv('Data/transitionMatrix.csv', names=states)
    q_df.index = states

    fig = plt.figure(figsize=(12, 12))
    ax = plt.subplot(111)
    ax.set_title('Graph - Shapes', fontsize=10)

    q = q_df.values

    # create state space and initial state probabilities
    states = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5']

    # print('\n', q, q.shape, '\n')
    # print(q_df.sum(axis=1))
    edges_wts = _get_markov_edges(q_df)
    # pprint(edges_wts)

    # create graph object
    G = nx.MultiDiGraph(format='jpeg')

    # nodes correspond to states
    G.add_nodes_from(states)

    # %print(f'Nodes:\n{G.nodes()}\n')
    # edges represent transition probabilities
    for k, v in edges_wts.items():
        tmp_origin, tmp_destination = k[0], k[1]
        if v!=0: G.add_edge(tmp_origin, tmp_destination, weight=v, label=v)
        # %print(f'Edges:')
        # %pprint(G.edges(data=True))

    pos = nx.drawing.nx_pydot.graphviz_layout(G, prog='dot')
    nx.draw_networkx(G, pos)

    # create edge labels for jupyter plot but is not necessary
    edge_labels = {(n1, n2): d['label'] for n1, n2, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.drawing.nx_pydot.write_dot(G, 'Output/markov.dot')

    text_from_file = str()
    # with open('markov.dot') as file:
    #    text_from_file = file.read()
    #    src = Source(text_from_file)
    #    src.render('markov_chain', view=True )

    plt.savefig('Output/MarkovGraph.png', format="PNG")
    plt.show()


# create a function that maps transition probability dataframe
# to markov edges and weights
def _get_markov_edges(Q):
    edges = {}
    for col in Q.columns:
        for idx in Q.index:
            edges[(idx, col)] = Q.loc[idx, col]
    return edges
