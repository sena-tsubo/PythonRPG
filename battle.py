try:
    from .ally import Ally
    from .enemy import Slime, Goblin
except ImportError:
    from ally.ally import Ally
    from enemy.enemy import Slime, Goblin


def build_battle_order(*fighters):
    return sorted(fighters, key=lambda fighter: fighter.speed, reverse=True)


def choose_target(current, allies, enemies):
    if current in allies:
        return next((enemy for enemy in enemies if enemy.is_alive()), None)
    return next((ally for ally in allies if ally.is_alive()), None)


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

    while any(a.is_alive() for a in allies) and any(e.is_alive() for e in enemies):
        for current in battle_order:
            if not current.is_alive():
                continue

            target = choose_target(current, allies, enemies)
            if target is None:
                continue

            print(f"\n[{current.name}のターン]")
            current.attack(target)

            if not any(a.is_alive() for a in allies) or not any(e.is_alive() for e in enemies):
                break

    if any(a.is_alive() for a in allies):
        print(f"\n{ally.name}たちの勝利です。")
    else:
        alive_enemy = next((enemy for enemy in enemies if enemy.is_alive()), None)
        winner_name = alive_enemy.name if alive_enemy else "敵"
        print(f"\n{winner_name}の勝利です。")


if __name__ == "__main__":
    main()
