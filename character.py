class Character:
    def __init__(self, name, health, power, speed, mp, magic_list=None):
        self.name = name
        self.health = health
        self.power = power
        self.speed = speed
        self.mp = mp
        self.max_mp = mp
        self.max_health = health
        self.magic = list(magic_list) if magic_list is not None else []
    
    def use_mp(self, amount):
        if self.mp >= amount:
            self.mp -= amount
            print(f"{self.name}は{amount}のMPを使用した。残りのMP: {self.mp}")
        else:
            print(f"{self.name}はMPが足りない。現在のMP: {self.mp}")

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name}は{amount}のダメージを受けた。残りの体力: {self.health}")
    
    def heal(self, amount):
        self.health += amount
        if  self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name}は{amount}回復した。現在の体力: {self.health}")

    def attack(self, target):
        damage = self.power
        print(f"{self.name}は{target.name}に{damage}のダメージを与えた。")
        target.take_damage(damage)



    def is_alive(self):
        return self.health > 0
    
    def info(self):
        print(f"名前:{self.name}\n体力:{self.health}\n攻撃力:{self.power}\nスピード:{self.speed}")
    #魔法を使用できるかどうかの判定を行う
