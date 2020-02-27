import json
import random
from mainAlgorithm.user import User
from mainAlgorithm.connection import Connection


def create_users_list():
    users_list = []
    with open('MOCK_DATA.json') as json_file:
        data = json.loads(json_file.read())
        for user in data:
            users_list.append(User(**user))

    return users_list


def create_connections_table(num_of_v):
    connections = [[0 for x in range(num_of_v)] for y in range(num_of_v)]
    for i in range(num_of_v):
        for j in range(num_of_v):
            if i < j and random.randint(0, 1):
                connections[i][j] = Connection(random.randint(1, 36), random.randint(0, 80))
            elif i < j:
                connections[i][j] = Connection(0, random.randint(0, 80))
            elif i == j:
                connections[i][j] = Connection(0, 0)
            else:
                connections[i][j] = connections[j][i]

    return connections


def creat_bool_connections(connections):
    bool_connections = [[False for x in range(len(connections))] for y in range(len(connections))]
    for i in range(len(connections)):
        for j in range(len(connections)):
            if connections[i][j].friendship_duration > 0 :
                bool_connections[i][j] = True

    return bool_connections