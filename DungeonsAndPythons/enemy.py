from unit import Unit


class Enemy(Unit):

    def __init__(self, health, mana, damage):
        self.damage = damage

        Unit.__init__(self, health, mana, damage)

    def __str__(self):
        return 'Enemy(health = ' + str(self.curr_health) + ', mana = ' + str(self.curr_mana) + ', ' + 'damage = ' + str(self.damage) + ')'
