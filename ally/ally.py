#味方側の基底クラス
try:
    from RPG.character import Character
    from RPG.magic.magic import Magic
except ImportError:
    from character import Character
    from magic.magic import Magic


class Ally(Character):
    def __init__(self, name, health, power, speed, mp):
        initial_magic = [
            Magic("ファイア", 10, 25),
            Magic("アイス", 8, 20),
            Magic("サンダー", 12, 30),
        ]
        super().__init__(name, health, power, speed, mp, magic_list=initial_magic)

    def attack(self, target):
        if not self.is_alive():
            return

        while True:
            command = self.select_command()
            if command == 1:
                super().attack(target)
                return
            if command == 2:
                if not self.available_magic():
                    print("使用可能な魔法がありません。")
                    continue
                self.select_magic(target)
                return
            if command == 3:
                print("アイテムを使用する処理をここに追加してください。")
                return

            print("無効な選択肢です。再度選択してください。")
            
    def available_magic(self):
        return [spell for spell in self.magic if spell.can_use(self)]
    
    def select_command(self):
        print(f"{self.name}のコマンドを選択してください。")
        print("1. 攻撃")
        print("2. 魔法")
        print("3. アイテム")
        choice = input("選択肢を入力してください: ")
        if choice not in {"1", "2", "3"}:
            print("無効な選択肢です。再度選択してください。")
            return self.select_command()
        return int(choice)

    def select_magic(self, target):
        usable_spells = self.available_magic()
        print(f"{self.name}の使用可能な魔法:")
        for index, spell in enumerate(usable_spells, start=1):
            print(f"{index}. {spell.name} (MP: {spell.mp_cost}, 威力: {spell.power})")
        print("0. 戻る")

        choice = input("使用する魔法を選択してください: ")
        if choice == "0":
            return self.attack(target)

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(usable_spells):
            print("無効な選択肢です。再度選択してください。")
            return self.select_magic(target)

        spell = usable_spells[int(choice) - 1]
        super().attack(target, magic=spell)

    def info(self):
        print(f"名前:{self.name}\n体力:{self.health}\n攻撃力:{self.power}\nスピード:{self.speed}\nMP:{self.mp}")
    
    def use_magic(self, spell, target):
        if not spell.can_use(self):
            print(f"{self.name}はMPが足りないため、{spell.name}を使用できません。")
            return False
        return super().attack(target, magic=spell)
