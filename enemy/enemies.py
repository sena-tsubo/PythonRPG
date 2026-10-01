import json
import random
from pathlib import Path

try:
    from .enemy import Goblin, Slime
except ImportError:
    from enemy.enemy import Goblin, Slime


ENEMY_CLASSES = {
    "slime": Slime,
    "goblin": Goblin,
}


def spawn_random_enemies():
    data_path = Path(__file__).parent.parent / "data" / "enemies.json"
    with data_path.open(encoding="utf-8") as file:
        enemy_data = json.load(file)

    enemy_count = random.randint(1, 2)
    enemies = []

    for data in random.choices(enemy_data, k=enemy_count):
        try:
            enemy_class = ENEMY_CLASSES[data["type"]]
        except KeyError as error:
            raise ValueError(f"未登録の敵タイプです: {data.get('type')}") from error

        enemies.append(
            enemy_class(
                data["name"],
                data["health"],
                data["power"],
                data["speed"],
                data["mp"],
            )
        )

    return enemies