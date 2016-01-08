from collections import deque
from panda import Panda


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

    def level(self, panda1, panda2):

        queue = deque([])
        visited = []
        level = 0


        if panda1 == panda2:
            return 0

        for item in self.graph[panda1]:
            if item not in visited:
                queue.append(item)
        while queue:

            for item in list(queue):
                if not item == panda2:
                    queue.popleft()
                    visited.append(item)
                    level += 1
                    if item in self.graph:
                        for element in self.graph[item]:
                            if element not in visited:
                                queue.append(element)
                else:
                   return level
        
        return level

    def how_many_gender_in_network(self, lev, panda, gender):
        queue = deque([])
        visited = []
        level = 0
        male_count = 0
        female_count = 0




        for item in self.graph[panda]:
            if item not in visited:
                queue.append(item)
        while queue:
            for item in list(queue):
                if level == lev:
                    if gender == 'male':
                        return male_count
                    else:
                        return female_count

                if not item == panda:

                    queue.popleft()
                    visited.append(item)
                    level += 1

                    if item.get_gender() == 'male':
                        male_count += 1
                    else:
                        female_count += 1
                    if item in self.graph:
                        for element in self.graph[item]:
                            if element not in visited:
                                queue.append(element)
        #         else:
        #            return level

        
        # return level



    def connection_level(self, panda1, panda2):
        if self.has_panda(panda1) == False or self.has_panda(panda2) == False:
            return False
        elif self.are_friends(panda1, panda2):
            return 1
        else:
            level = self.level(panda1, panda2)
            return level

    def are_connected(self, panda1, panda2):
        if not self.connection_level(panda1, panda2) == False:
            print("COnnected")
            return True
        else:
            return False



pesho = Panda("Pesho", "dwadwa", "male")
gosho = Panda("GOsho", "dwadwa", "male")
peshka = Panda("Peshka", "dwaeqw", "female")
misho = Panda("Gdwa", "dwadwa", "female")
spas = Panda("Peswq", "dwaeqw", "male")

network = SocialNetwork()

network.add_panda(pesho)
network.add_panda(gosho)
network.add_panda(peshka)

# network.add_panda(pesho)
print(network.has_panda(pesho))
network.make_friends(pesho, gosho)
network.make_friends(gosho, peshka)
network.make_friends(peshka, misho)
network.make_friends(misho, spas)
print(network.are_friends(pesho, peshka))
print(network.friends_of(pesho))
print(network.connection_level(pesho, spas))
print(network.how_many_gender_in_network(2, gosho, 'male'))
