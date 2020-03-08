import pickle
from create_data import *


def main():
    users_list = create_users_list()
    print("uer, u")
    for u in users_list:
        print (u.id, u.u)
    num_of_v = len(users_list)
    connections = create_connections_table(num_of_v)
    print("vertix1 vertix 2, c")
    for i in range(num_of_v-1):
        for j in range(i+1, num_of_v):
            print(i, j, connections[i][j].c)
    bool_connections = create_bool_connections(connections)
    users = open('user_list', 'wb')
    pickle.dump(users_list, users)
    connection = open('connections', 'wb')
    pickle.dump(connections, connection)
    bool_connection = open('bool_connections', 'wb')
    pickle.dump(bool_connections, bool_connection)
    users.close()
    connection.close()
    bool_connection.close()


if __name__ == "__main__":
    main()
