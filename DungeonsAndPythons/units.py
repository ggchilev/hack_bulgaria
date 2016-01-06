from spell import Spell


class Unit:

    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

        self.curr_health = health
        self.curr_mana = mana

    def is_alive(self):
        return self.curr_health > 0

    def can_cast(self, spell):
        if self.curr_mana > spell.mana_cost:
            print('Can cast')
            return True
        else:
            print("NOT ENOUGH MANA!!!")
            return False

    def get_health(self):
        return self.curr_health

    def get_mana(self):
        return self.curr_mana

    def take_damage(self, damage_points):
        if damage_points >= self.curr_health:
            self.curr_health = 0
            return self.curr_health
        else:
            self.curr_health -= damage_points
            return self.curr_health

    def take_healing(healing_points):
        if self.is_alive() == False:
            print('It is too late to heal our hero')
            return False
        else:
            if (selh.curr_health + healing_points) <= self.health:
                self.curr_health += healing_points
                print('Healing successful')
                return True
            else:
                print('We cannot heal our hero above the maximum health')
                return False

          