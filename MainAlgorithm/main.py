from MainAlgorithm.find_trusworthy_netwotk import *
import pickle

def main():
    # open a file, where you stored the pickled data
    file_users = open('/home/aviv/PycharmProjects/BigDataMiniProject/CreateData/user_list', 'rb')
    users_list = pickle.load(file_users)
    file_users.close()
    file_connections = open('/home/aviv/PycharmProjects/BigDataMiniProject/CreateData/connections', 'rb')
    connections = pickle.load(file_connections)
    file_connections.close()
    file_bool_connections = open('/home/aviv/PycharmProjects/BigDataMiniProject/CreateData/bool_connections', 'rb')
    bool_connections = pickle.load(file_bool_connections)
    file_bool_connections.close()
    num_of_v = len(users_list)

    ego_node = input("Enter ego node - a number between 1 to 60 :")
    # plot_new_graph(num_of_v, bool_connections, ego_node)
    mtv = input("Enter minimum trust value : ")
    copy_bool_connections = deepcopy(bool_connections)
    find_trustworthy_network(users_list, connections, mtv, ego_node, copy_bool_connections)


if __name__ == "__main__":
    main()
