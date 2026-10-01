# 味方側の基底クラスです。
try:
    from RPG.character import Character
    from RPG.magic.magic import Magic, RecoveryMagic
except ImportError:
    from character import Character
    from magic.magic import Magic, RecoveryMagic
#3. 味方キャラクターの基底クラスを作成します。

class Ally(Character):
    # プレイヤーが操作する味方キャラクターです。
    # 攻撃・魔法・アイテムの選択を行います。

    def __init__(self, name, health, power, speed, mp):
        initial_magic = [
            Magic("ファイア", 10, 25),
            Magic("アイス", 8, 20),
            Magic("サンダー", 12, 30),
            RecoveryMagic("ヒール", 5, 30),
        ]
        super().__init__(name, health, power, speed, mp, magic_list=initial_magic)

    def attack(self, target):
        # 戦闘中のコマンド選択を行います。
        if not self.is_alive():
            return

        while True:
            command = self.select_command()
            if command == 1:
                super().attack(target)
                return
            elif command == 2:
                if not self.available_magic():
                    print("使用可能な魔法がありません。")
                    continue
                self.select_magic(target)
                return
            elif command == 3:
                print("アイテムを使用する処理をここに追加してください。")
                return
            else:
                print("無効な選択肢です。再度選択してください。")
                return
    def choose_target(self, enemies):
        # 攻撃対象を選びます。
        print(f"{self.name}の攻撃対象を選択してください。")
        for index, enemy in enumerate(enemies):
            print(f"{index+1}. {enemy.name} (体力: {enemy.health})")
        choice = input("攻撃対象の番号を入力してください: ")
        #isdigit()メソッドは、文字列が数字のみで構成されているかどうかを判定するためのメソッドです。
        #文字列が数字のみで構成されている場合はTrueを返し、そうでない場合はFalseを返します。
        if not choice.isdigit():
            print("無効な選択肢です。再度選択してください。")
            return self.choose_target(enemies)

        target_index = int(choice) - 1
        if target_index < 0 or target_index >= len(enemies):
            print("無効な選択肢です。再度選択してください。")
            return self.choose_target(enemies)

        self.attack(enemies[target_index])
    def available_magic(self):
        # 使える魔法だけを取り出します。
        usable_magic = []
        for spell in self.magic:
            if spell.can_use(self):
                usable_magic.append(spell)
        return usable_magic

    def select_command(self):
        # どの行動を取るかを選びます。
        print(f"{self.name}のコマンドを選択してください。")
        print("1. 攻撃")
        print("2. 魔法")
        print("3. アイテム")
        choice = input("選択肢を入力してください: ")
        if choice not in ["1", "2", "3"]:
            print("無効な選択肢です。再度選択してください。")
            return self.select_command()
        return int(choice)

    def select_magic(self, target):
        # 使用する魔法を選びます。
        usable_spells = self.available_magic()
        print(f"{self.name}の使用可能な魔法:")

        index = 1
        for spell in usable_spells:
            print(f"{index}. {spell.name} (MP: {spell.mp_cost}, 威力: {spell.power})")
            index += 1
        print("0. 戻る")

        choice = input("使用する魔法を選択してください: ")
        if choice == "0":
            self.attack(target)
            return

        if not choice.isdigit():
            print("無効な選択肢です。再度選択してください。")
            self.select_magic(target)
            return

        spell_number = int(choice)
        if spell_number < 1 or spell_number > len(usable_spells):
            print("無効な選択肢です。再度選択してください。")
            self.select_magic(target)
            return

        spell = usable_spells[spell_number - 1]
        spell.use(self, target)

    def info(self):
        # 味方キャラクターの情報を表示します。
        print(f"名前:{self.name}\n体力:{self.health}\n攻撃力:{self.power}\nスピード:{self.speed}\nMP:{self.mp}")


