class Magic:
    def __init__(self, name, mp_cost, power):
        self.name = name
        self.mp_cost = mp_cost
        self.power = power

    def use(self, caster, target):
        if self.can_use(caster):
            caster.use_mp(self.mp_cost)
            damage = self.power
            print(f"{caster.name}は{self.name}を使用し、{target.name}に{damage}のダメージを与えた。")
            target.take_damage(damage)
            return True

        return False

    def info(self):
        print(f"魔法名: {self.name}\nMP消費: {self.mp_cost}\n威力: {self.power}")

    def can_use(self, caster):
        return caster.mp >= self.mp_cost