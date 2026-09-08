try:
    from .ally import Ally
    from .enemy import Slime, Goblin
except ImportError:
    from ally.ally import Ally
    from enemy.enemy import Slime, Goblin


def build_battle_order(*fighters):
    # 速いキャラクターから順に並べるための関数です。
    ordered = list(fighters)
    count = len(ordered)

    for i in range(count):
        for j in range(0, count - i - 1):
            if ordered[j].speed < ordered[j + 1].speed:
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]

    return ordered


def choose_target(current, allies, enemies):
    # そのキャラクターが攻撃する相手を選びます。
    if current in allies:
        for enemy in enemies:
            if enemy.is_alive():
                return enemy
        return None

    for ally in allies:
        if ally.is_alive():
            return ally
    return None


def has_living_fighter(fighters):
    # 1人でも生存しているキャラクターがいるか確認します。
    for fighter in fighters:
        if fighter.is_alive():
            return True
    return False
#敵キャラクターをランダムでスポーンさせる関数を追加します。

def main():
    print("=== RPG バトル開始 ===")
    ally = Ally("勇者", 150, 20, 10, 30)
    slime = Slime("スライム", 50, 10, 5, 0)
    goblin = Goblin("ゴブリン", 80, 15, 8, 0)

    allies = [ally]
    enemies = [slime, goblin]
    battle_order = build_battle_order(ally, slime, goblin)

    print("戦闘順:")
    for fighter in battle_order:
        print(f"- {fighter.name} (Speed: {fighter.speed})")

    while has_living_fighter(allies) and has_living_fighter(enemies):
        for current in battle_order:
            if not current.is_alive():
                continue

            target = choose_target(current, allies, enemies)
            if target is None:
                continue

            print(f"\n[{current.name}のターン]")
            current.attack(target)

            if not has_living_fighter(allies) or not has_living_fighter(enemies):
                break

    if has_living_fighter(allies):
        print(f"\n{ally.name}たちの勝利です。")
    else:
        alive_enemy = None
        for enemy in enemies:
            if enemy.is_alive():
                alive_enemy = enemy
                break

        winner_name = alive_enemy.name if alive_enemy is not None else "敵"
        print(f"\n{winner_name}の勝利です。")


if __name__ == "__main__":
    main()
