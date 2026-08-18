class Character:
    # キャラクターの基本的な能力と行動をまとめたクラスです。
    # 体力・攻撃力・MP・魔法の情報を持ちます。
    #１．基底クラスを作成します。
    def __init__(self, name, health, power, speed, mp, magic_list=None):
        self.name = name
        self.health = health
        self.power = power
        self.speed = speed
        self.mp = mp
        self.max_mp = mp
        self.max_health = health
        self.magic = []

        if magic_list is not None:
            for magic in magic_list:
                self.magic.append(magic)

    def use_mp(self, amount):
        # MPを使う処理です。MPが足りないときは使えません。
        if self.mp >= amount:
            self.mp -= amount
            print(f"{self.name}は{amount}のMPを使用した。残りのMP: {self.mp}")
        else:
            print(f"{self.name}はMPが足りない。現在のMP: {self.mp}")

    def take_damage(self, amount):
        # ダメージを受けたときの処理です。
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name}は{amount}のダメージを受けた。残りの体力: {self.health}")

    def heal(self, amount):
        # 回復するときの処理です。体力が上限を超えないようにします。
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name}は{amount}回復した。現在の体力: {self.health}")

    def attack(self, target, magic=None):
        # 通常攻撃か、魔法攻撃かを切り替えて処理します。
        if magic is not None:
            magic.use(self, target)
            return

        damage = self.power
        print(f"{self.name}は{target.name}に{damage}のダメージを与えた。")
        target.take_damage(damage)

    def is_alive(self):
        # 生存しているかどうかを確認します。
        return self.health > 0

    def info(self):
        # 画面にキャラクター情報を表示します。
        print(f"名前:{self.name}\n体力:{self.health}\n攻撃力:{self.power}\nスピード:{self.speed}\nMP:{self.mp}")
