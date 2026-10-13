try:
    from .ally.ally import Ally
    from .enemy.enemies import spawn_random_enemies
except ImportError:
    from ally.ally import Ally
    from enemy.enemies import spawn_random_enemies


def build_battle_order(*fighters):
    # 速いキャラクターから順に並べるための関数です。
    ordered = list(fighters)
    count = len(ordered)

    for i in range(count):
        for j in range(0, count - i - 1):
            if ordered[j].speed < ordered[j + 1].speed:
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]

    return ordered


def has_living_fighter(fighters):
    # 1人でも生存しているキャラクターがいるか確認します。
    for fighter in fighters:
        if fighter.is_alive():
            return True
    return False


def main():
    print("=== RPG バトル開始 ===")
    ally = Ally("勇者", 150, 20, 10, 30)
    allies = [ally]
    enemies = spawn_random_enemies()
    battle_order = build_battle_order(*allies, *enemies)

    print("戦闘順:")
    for fighter in battle_order:
        print(f"- {fighter.name} (Speed: {fighter.speed})")

    while has_living_fighter(allies) and has_living_fighter(enemies):
        for current in battle_order:
            if not current.is_alive():
                continue

            print(f"\n[{current.name}のターン]")
            if isinstance(current , Ally):
                current.choose_target(enemies)
            else:
                current.choose_target(allies)

            if not has_living_fighter(allies) or not has_living_fighter(enemies):
                break

    if has_living_fighter(allies):
        print(f"\n{ally.name}たちの勝利です。")
    else:
        print("\n敵の勝利です。")

#__name__ == "__main__": はPythonで必要な処理の実行を制御するための条件文です。スクリプトが直接実行された場合にのみ、main()関数を呼び出すようにしています。これにより、他のモジュールからインポートされた場合にはmain()が自動的に実行されることを防ぎます。
if __name__ == "__main__":
    main()
