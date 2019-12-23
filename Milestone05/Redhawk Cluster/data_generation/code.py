import pandas as pd
import numpy as np
import networkx as nx
import statistics
from multiprocessing import Process
from datetime import datetime

def get_degrees(G):
    deg = nx.degree_centrality(G)
    deg_df = pd.Series(deg).to_frame()
    deg_df.columns = ['Degree']
    deg_df['degree_rank'] = deg_df['Degree'].rank(method = 'min', ascending = False)
    return deg_df

def get_closeness(G):
    deg = nx.closeness_centrality(G)
    deg_df = pd.Series(deg).to_frame()
    deg_df.columns = ['Closeness']
    deg_df['closeness_rank'] = deg_df['Closeness'].rank(method = 'min', ascending = False)
    return deg_df

def get_betweeness(G):
    deg = nx.betweenness_centrality(G)
    deg_df = pd.Series(deg).to_frame()
    deg_df.columns = ['Betweeness']
    deg_df['betweeness_rank'] = deg_df['Betweeness'].rank(method = 'min', ascending = False)
    return deg_df

def get_load_flow(G):
    deg = nx.load_centrality(G)
    deg_df = pd.Series(deg).to_frame()
    deg_df.columns = ['Load']
    deg_df['load_rank'] = deg_df['Load'].rank(method = 'min', ascending = False)
    return deg_df

def get_local_reaching(G):
    deg = {}
    for x in range(len(G)): # compute local reach centrality for each node in G
        deg[x] = nx.local_reaching_centrality(G, x)
    deg_df = pd.Series(deg).to_frame()
    deg_df.columns = ['Reaching']
    deg_df['reach_rank'] = deg_df['Reaching'].rank(method = 'min', ascending = False)
    return deg_df

def get_harmonic(G):
    deg = nx.harmonic_centrality(G)
    deg_df = pd.Series(deg).to_frame()
    deg_df.columns = ['Harmonic']
    deg_df['harmonic_rank'] = deg_df['Harmonic'].rank(method = 'min', ascending = False)
    return deg_df

def get_page_rank(G):
    deg = nx.pagerank_scipy(G)
    deg_df = pd.Series(deg).to_frame()
    deg_df.columns = ['Page']
    deg_df['page_rank'] = deg_df['Page'].rank(method = 'min', ascending = False)
    return deg_df

def get_average_distance(G):
    length = dict(nx.all_pairs_shortest_path_length(G)).values()
    means = []
    for val in length:
        means.append(statistics.mean(val))
    return statistics.mean(means)

def get_average_clustering(G):
    G2 = nx.DiGraph(G)
    return nx.average_clustering(G2)

def get_number_cliques(G):
    G2 = G.to_undirected()
    return nx.graph_clique_number(G2);

def get_strongly_connected(G):
    G2 = nx.DiGraph(G)
    return nx.number_strongly_connected_components(G2)


def parallel_generation(netType, size):
    
    def inner_split(netType, size, processNum):
        with open(netType.replace('/','-') + '/' + str(size) + '/' + str(processNum), 'w') as clearfile:
            pass # this clears the file so that we can view progress throughout the job
        for instNum in range((processNum*2) - 1, (processNum*2) + 1): # each process handles 2 networks
            if netType == 'scale-free':
                G = nx.scale_free_graph(size)
            elif netType == 'small-world':
                G = nx.watts_strogatz_graph(size, 3, 0.5)
            elif netType == 'small-world/scale-free':
                G = nx.powerlaw_cluster_graph(size, 3, 0.5)
            else:
                G = nx.gnm_random_graph(size, size * 4)

            degree_list = get_degrees(G)
            closeness_list = get_closeness(G)
            betweeness_list = get_betweeness(G)
            load_list = get_load_flow(G)
            reach_list = get_local_reaching(G)
            harmonic_list = get_harmonic(G)
            page_list = get_page_rank(G)
            distance_list = get_average_distance(G)
            clustering_list = get_average_clustering(G)
            cliques_list = get_number_cliques(G)
            redundancy_list = get_number_cliques(G)

            for node in G.nodes():
                with open(netType.replace('/','-') + '/' + str(size) + '/' + str(processNum), 'a') as outfile:
                    outfile.write(netType + ',' + str(size)+ ',' + str(instNum) + ',')
                    outfile.write(str(node) + ',' + str(degree_list['degree_rank'][node]) + ',')
                    outfile.write(str(closeness_list['closeness_rank'][node]) + ',')
                    outfile.write(str(betweeness_list['betweeness_rank'][node]) + ',')
                    outfile.write(str(load_list['load_rank'][node]) + ',')
                    outfile.write(str(reach_list['reach_rank'][node]) + ',')
                    outfile.write(str(harmonic_list['harmonic_rank'][node]) + ',')
                    outfile.write(str(page_list['page_rank'][node]) + ',')
                    outfile.write(str(get_average_distance(G)) + ',')
                    outfile.write(str(get_average_clustering(G)) + ',')
                    outfile.write(str(get_number_cliques(G)) + ',')
                    outfile.write(str(get_strongly_connected(G)) + '\n')
        # end inner_split()
        
    processes = [0]*25
    for processNum in range(1, 26): # generate 25 2-network processes for each size and each network type (50 total networks)
        processes[processNum - 1] = Process(target=inner_split, args=(netType, size, processNum))
        processes[processNum - 1].start() # deploy each of the 25 processes
    
    for i in range(len(processes)): # wait for all processes to finish
        processes[i].join()

print('Started: ' + datetime.now().strftime('%m-%d %H:%M:%S') + '\n')
parallel_generation('small-world/scale-free', 800)
print('Finished: ' + datetime.now().strftime('%m-%d %H:%M:%S') + '\n')
