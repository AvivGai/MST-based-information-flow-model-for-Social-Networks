from copy import deepcopy
from MainAlgorithm.kruskal import kruskal
from MainAlgorithm.bfs import *
import networkx as nx
import matplotlib.pyplot as plt


def find_first_degree_friends(ego_node, num_of_v, connections):
    friends = []
    for i in range(num_of_v):
        if connections[ego_node][i].friendship_duration > 0:
            friends.append(i)

    return friends


def create_sub_graph(node, num_of_v, connections):
    edges_list = []
    vertices_list = []

    # create vertices list and edges for first degree friends of "node"
    for i in range(num_of_v):
        if connections[node][i].friendship_duration > 0:
            vertices_list.append(i)
            edges_list.append((connections[node][i].c, node, i))

    # create edges for friendships between all friends of "node"
    for i in range(len(vertices_list) - 1):
        for j in range(i + 1, len(vertices_list)):
            node1 = vertices_list[i]
            node2 = vertices_list[j]
            if connections[node1][node2].friendship_duration > 0:
                edges_list.append((connections[node1][node2].c, node1, node2))
    vertices_list.append(node) # add the node itself to the vertices list
    sub_graph = {'vertices': vertices_list, 'edges': edges_list}
    return sub_graph


def find_and_remove_isolated_nodes(sub_graph, mst, node, users_list, bool_connections, MTV):
    copy_sub_graph = deepcopy(sub_graph) # create a copy of the graph
    for edge in mst:
        list(copy_sub_graph['edges']).remove(edge) # remove from the graph edges that are part of mst
    visited = bfs(copy_sub_graph, node)
    for v, is_visit in visited.items():
        if not is_visit:
            if users_list[v].u < MTV: # for every vertice that: not visited in the bfs & u < MTV
                for edge in list(sub_graph['edges']):
                    c, x1, x2 = edge
                    if v == x1 or v == x2:
                        bool_connections[x1][x2] = False
                        bool_connections[x2][x1] = False


def plot_new_graph(num_of_v, bool_connections, ego_node):
    g = nx.Graph()
    g.add_node(num_of_v)
    for i in range(num_of_v - 1):
        for j in range(i + 1, num_of_v):
            if bool_connections[i][j]:
                g.add_edge(i, j)
    nodes = g.nodes

    ego_graph = nx.ego_graph(g, int(ego_node), 2, True)
    plt.figure(figsize=(20, 20))
    pos = nx.spring_layout(ego_graph)
    nx.draw(ego_graph, pos, with_labels=True, node_size=6000, node_color="skyblue", node_shape="s", alpha=0.5,
            linewidths=80, font_size=70)
    nx.draw_networkx_nodes(ego_graph, pos, nodelist=[int(ego_node)], node_size=15000, node_color='r')
    plt.savefig("trustworthy network.png")

    # l1 = []
    # l2 = []
    # for i in range(num_of_v - 1):
    #     for j in range(i + 1, num_of_v):
    #         if bool_connections[i][j]:
    #             l1.append(i)
    #             l2.append(j)
    # # Build a dataframe with your connections
    # df = pd.DataFrame({'from': l1, 'to': l2})
    #
    #
    # # Build your graph
    # G = nx.from_pandas_edgelist(df, 'from', 'to')
    # ego_graph = nx.ego_graph(G, ego_node)
    # # Graph with Custom nodes:
    # plt.figure(figsize=(20, 20))
    #
    # nx.draw(ego_graph, with_labels=True, node_size=6000, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=80, font_size = 70)
    # plt.savefig("foo"+str(num)+".png")


def find_trustworthy_network(users_list, connections, mtv, ego_node, bool_connections):
    mtv = float(mtv)
    ego_node = int(ego_node)
    num_of_v = len(users_list)
    ego_node_first_degree_friends = find_first_degree_friends(ego_node, num_of_v, connections)
    for v in ego_node_first_degree_friends:
        sub_graph = create_sub_graph(v, num_of_v, connections)
        num_of_v_in_sub_graph = len(sub_graph['vertices'])
        mst = kruskal(sub_graph, num_of_v_in_sub_graph)
        find_and_remove_isolated_nodes(sub_graph, mst, v, users_list, bool_connections, mtv)

    plot_new_graph(num_of_v, bool_connections, ego_node)
