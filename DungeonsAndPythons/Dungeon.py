from random import randint
from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell
import sys


class Dungeon:


    def __init__(self, filename):
        self._filename = filename
        self._is_found = False


    def _read_dungeon(self):

        dungeon = [[]]
        with open(self._filename, 'r') as data:
            dungeon = [list(item) for line in data for item in line.split()]
        
        return dungeon

    def _wtire_dungeon(self, dungeon):
        data = open(self._filename, 'w')
        for item in dungeon:
            data.write(''.join(item)+"\n")

    def _print_map(self):
        my_list = []
        dungeon_map = self._read_dungeon()
        for row in range(0, len(dungeon_map)):
            for col in range(0, len(dungeon_map[row])):
                my_list.append(dungeon_map[row][col])
            print(''.join(my_list))
            my_list = []


    def _spawn(self, hero):
        my_list = []
        dungeon = self._read_dungeon()
        for row in range(0, len(dungeon)):
            for col in range(0, len(dungeon[row])):
                if dungeon[row][col] == 'H':
                    dungeon[row][col] = '.'
                    self._is_found = False
                elif self._is_found == False and (dungeon[row][col] == 'S' or dungeon[row][col] == '.'):
                    dungeon[row][col] = 'H'
                    self._is_found = True
        self._wtire_dungeon(dungeon)

        return dungeon

     
    def check(self, place):
        if place == 'T':
            print('Found treasure')
            return True
        elif place == '#':
            return False
            print('Ooops, obstcale')
            return False
        elif place == 'E':
            print('A fight between ' + str(hero) + ' and ' + str(enemy) + 'has started')
            map.hero_attack(by='spell')
            return True
        elif place == 'G':
            print('-----------------------You Win ---------------------------')
            return True
        else:
            print('Nice')
            return True

    def _move_up(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'H':
                    if row == 0 :
                        return False
                    elif self.check(my_map[row-1][col]):
                        my_map[row-1][col] = 'H'
                        my_map[row][col] = '.'
                        self._wtire_dungeon(my_map)
                        hero.curr_mana += hero.mana_regen
                        return True
                    else:
                        return False

    def _move_down(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'H':
                    if row == len(my_map)-1 :
                        return False
                    elif self.check(my_map[row+1][col]):
                        my_map[row+1][col] = 'H'
                        my_map[row][col] = '.'
                        self._wtire_dungeon(my_map)
                        hero.curr_mana += hero.mana_regen
                        return True
                    else:
                        return False

    def _move_right(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'H':
                    if row == len(my_map[row])-1 :
                        return False
                    elif self.check(my_map[row][col+1]):
                        my_map[row][col+1] = 'H'
                        my_map[row][col] = '.'
                        self._wtire_dungeon(my_map)
                        hero.curr_mana += hero.mana_regen
                        return True
                    else:
                        return False


    def _move_left(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'H':
                    if row == 0 :
                        return False
                    elif self.check(my_map[row][col-1]):
                        my_map[row][col-1] = 'H'
                        my_map[row][col] = '.'
                        self._wtire_dungeon(my_map)
                        hero.curr_mana += hero.mana_regen
                        return True
                    else:
                        return False



    def _move_hero(self, direction):
        if direction == 'up':
            print(self._move_up())
        if direction == 'down':
            print(self._move_down())
        if direction == 'right':
            print(self._move_right())
        if direction == 'left':
            print(self._move_left())

    def _read_treasures(self):
        filename = 'treasures.txt'
        with open(filename, 'r') as data:
            treasures = [item for line in data for item in line.split()]
        return treasures



    def _pick_treasure(self):
        treasures = self._read_treasures()
        num = randint(0, len(treasures)-1)
        print(treasures[num])

    def hero_attack(self, by):
        if by == 'spell':
            while hero.curr_health > 0 and enemy.curr_health > 0:
                if hero.magic_damage > 0 and hero.curr_mana >= s.mana_cost:
                    enemy.curr_health -= hero.magic_damage
                    hero.curr_mana -= s.mana_cost
                    print('Hero attacks with spell. Enemy`s health is reduced to ' + str(enemy.curr_health))
                    if enemy.is_alive():
                        hero.curr_health -= enemy.damage
                        print('Enemy attacks. Hero`s health is reduced to ' + str(hero.curr_health))
                        if hero.is_alive() == False:
                            print('GAME OVER')
                            sys.exit(0)
                    else:
                        print('enemy is dead')
                        return True
                if hero.curr_health > 0 and hero.curr_mana < s.mana_cost:
                    by = 'weapon'
                    print('Hero is out of mana')
                    break

        if by == 'weapon':

            while hero.curr_health > 0 and enemy.curr_health > 0:
                if hero.phisical_damage > 0:
                    print('willy')
                    enemy.curr_health -= hero.phisical_damage
                    print('Hero attacks with ' + w.name + '. Enemy`s health is reduced to ' + str(enemy.curr_health))
                    if enemy.is_alive():
                        hero.curr_health -= enemy.damage
                        print('Enemy attacks. Hero`s health is reduced to ' + str(hero.curr_health))
                        if hero.is_alive() == False:
                            print('GAME OVER')
                            sys.exit(0)
                    else:
                        print('enemy is dead')
                        return True
        else:
            print('The hero can use only spell or weapon')





map = Dungeon('dungeon.txt')
hero = Hero(name = 'Django', title = 'The Unchained', health = 100, mana = 100, mana_regen  = 2)
enemy = Enemy(health = 80, mana = 100, damage = 20)
w = Weapon('Axe', 20)
s = Spell('Magic', 20, 50, 2)
hero.equip(w)
hero.learn(s)

print(hero.get_health())
print(enemy.get_health())

map._pick_treasure()


map._print_map()
map._spawn('Batman')
map._move_hero('right')
map._print_map()
map._move_hero('down')
map._print_map()
map._move_hero('down')
map._print_map()
map._move_hero('down')
map._print_map()
map._move_hero('right')
map._print_map()
map._move_hero('right')
map._print_map()
map._move_hero('right')
map._print_map()
map._move_hero('right')
map._print_map()
map._move_hero('right')
map._print_map()
map._move_hero('right')
map._print_map()
map._move_hero('right')
map._print_map()
map._move_hero('down')
map._print_map()
map._move_hero('right')
map._print_map()
#print(hero.curr_mana)
#map._spawn('Batman')
#map._print_map()
