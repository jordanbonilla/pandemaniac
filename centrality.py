#!/usr/bin/env python2

import networkx as nx
import numpy as np
from operator import itemgetter

def generate_seeds(num_players, num_seeds, G):
    # Initialize see array to zeros
    seeds = np.zeros(num_seeds, dtype=np.int)

    m = nx.closeness_centrality(G);

    sorted_centralities = sorted(m.items(), key=itemgetter(1), reverse=True)

    for i in range(num_seeds):
        seeds[i] = sorted_centralities[i][0]

    return seeds
