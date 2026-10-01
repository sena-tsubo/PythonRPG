try:
    from RPG.character import Character
except ImportError:
    from character import Character
# *--------2. 敵キャラクターの基底クラスを作成します。--------*

class Enemy(Character):
    # 敵キャラクターの基底クラスです。
    def __init__(self, name, health, power, speed, mp):
        super().__init__(name, health, power, speed, mp)
    def choose_target(self , allies):
        #攻撃対象を選びます。敵は自動で生存している味方を選びます。
        if not self.is_alive():
            return

        for ally in allies:
            if ally.is_alive():
                self.attack(ally)
                return

class Slime(Enemy):
    # 体力が低くなると回復するスライムです。
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
    


class Goblin(Enemy):
    # 体力が低くなると攻撃力が上がるゴブリンです。
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

