try:
    from RPG.character import Character
except ImportError:
    from character import Character


class Enemy(Character):
    def __init__(self, name, health, power, speed, mp):
        super().__init__(name, health, power, speed, mp)

#スライムクラスの説明。
class Slime(Enemy):
    def __init__(self, name, health, power, speed, mp):
        super().__init__(name, health, power, speed, mp)
        self.heal_threshold = 0.5
        self.heal_amount = 15
        self.heal_used = False

    def attack(self, target):
        if self.health <= self.max_health * self.heal_threshold and not self.heal_used:
            self.heal(self.heal_amount)
            self.heal_used = True
        else:
            super().attack(target)

#ゴブリンクラスの説明。
class Goblin(Enemy):
    def __init__(self, name, health, power, speed, mp):
        super().__init__(name, health, power, speed, mp)
        self.power_threshold = 0.3
        self.power_up_amount = 15
        self.power_up_used = False

    def attack(self, target):
        if self.health <= self.max_health * self.power_threshold and not self.power_up_used:
            self.power += self.power_up_amount
            self.power_up_used = True
        else:
            super().attack(target)

