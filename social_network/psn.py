from collections import deque
from panda import Panda
import json


class Panda:

    def __init__(self, name, email, gender):
        self._name = name
        self._email = email
        self._gender = gender

        self.friend_list = set()

    def __str__(self):
        return 'Panda ' + self._name

    def __hash__(self):
        return 2

    def __eq__(self, other):
        if self._name == other._name and self._email == other._email and self._gender == other._gender:
            return True
        else:
            return False

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender



class SocialNetwork:

    def __init__(self):

        self.panda_list = []
        self.graph = {}

    def __hash__(self):
        return 1

    def add_panda(self, panda):
        if panda not in self.graph:
            self.graph[panda] = panda.friend_list
            return True
        else:
            print('Panda ' + panda.get_name() +
                  ' is already in the Social Network')
            return False

    def has_panda(self, panda):
        if panda in self.graph:
            return True
        else:
            return False

    def make_friends(self, panda1, panda2):
        if panda1 not in self.graph:
            self.graph[panda1] = panda1.friend_list
        if panda2 not in self.graph:
            self.graph[panda2] = panda2.friend_list
        panda1.friend_list.add(panda2)
        panda2.friend_list.add(panda1)

    def are_friends(self, panda1, panda2):
        if panda1 in panda2.friend_list and panda2 in panda1.friend_list:
            return True
        else:
            return False

    def friends_of(self, panda):
        if panda not in self.graph:
            return False
        else:
            my_list = []
            for item in panda.friend_list:
                my_list.append(str(item))
            return my_list

    def bfs_with_level(self, start_node, end_node):
    
        visited = set()
        queue = deque()

        visited.add(start_node)
        queue.append((0, start_node))

        while len(queue) != 0:
            node_with_level = queue.popleft()
            node = node_with_level[1]
            level = node_with_level[0]

            if node == end_node:
                return level

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))

        return -1

    def how_many_gender_in_network(self, lev, panda, gender):
    
        visited = set()
        queue = deque()
        male_count = 0
        female_count = 0

        visited.add(panda)
        queue.append((0, panda))

        while len(queue) != 0:
            node_with_level = queue.popleft()
            node = node_with_level[1]
            level = node_with_level[0]

            if level == lev:
                if gender == 'male':
                    return male_count
                else:
                    return female_count

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))
                    if neighbour.get_gender() == 'male':
                        male_count += 1
                    else:
                        female_count += 1

        return -1


    def connection_level(self, panda1, panda2):
        if self.has_panda(panda1) == False or self.has_panda(panda2) == False:
            return False
        elif self.are_friends(panda1, panda2):
            return 1
        else:
            level = self.bfs_with_level(panda1, panda2)
            return level

    def are_connected(self, panda1, panda2):
        if not self.connection_level(panda1, panda2) == False:
            print("COnnected")
            return True
        else:
            return False

    def graph_to_string(self):
        my_dic = {}
        my_list = []
        for panda in self.graph:
            for friend in self.graph[panda]:
                my_list.append(str(friend))
            my_dic[str(panda)] = my_list
            my_list = []
        return my_dic

    def string_to_graph(self):
        my_dic = {}
        my_list = []
        for panda in pandas:
            for friend in panda:
                my_list.append[friend]


    def save(self, file_name):

        panda_dic = self.graph_to_string()

        with open('socialNetwork.json', 'w') as f:
            json.dump(panda_dic, f)


    def load(self, file_name):

        with open('socialNetwork.json', "r") as f:
            data = json.load(f)
            f.close()

        for key, value in data.items():
            key_split = key.split(',')
            self.graph[Panda(key_split[0],'da','dwa')] = []
            for v in value:
                v_split = v.split(',')
                self.graph[Panda(key_split[0], 'da', 'dwa')
                              ].append(Panda(v_split[0], 'da', 'dwa'))

        return data

