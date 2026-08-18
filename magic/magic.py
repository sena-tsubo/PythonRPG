class Magic:
    # 魔法の名前・消費MP・威力を持つクラスです。
    # 
    def __init__(self, name, mp_cost, power):
        self.name = name
        self.mp_cost = mp_cost
        self.power = power

    def use(self, caster, target):
        # 魔法を使うときの処理です。
        if self.can_use(caster):
            caster.use_mp(self.mp_cost)
            damage = self.power
            print(f"{caster.name}は{self.name}を使用し、{target.name}に{damage}のダメージを与えた。")
            target.take_damage(damage)
            return True

        return False

    def info(self):
        # 魔法の情報を表示します。
        print(f"魔法名: {self.name}\nMP消費: {self.mp_cost}\n威力: {self.power}")

    def can_use(self, caster):
        # その魔法を使えるかどうかを確認します。
        return caster.mp >= self.mp_cost