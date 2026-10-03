# Text-Based Battle Game

A simple turn-based command-line fighting game written in Python. Choose an enemy, battle it round by round, earn levels, heal up, and spend your levels on stronger weapons.

## Features

- Turn-based combat against three enemies of increasing difficulty
- Level system where levels act as both your progress and your currency
- Healing system (costs a level)
- Weapon shop with four weapons to unlock
- Replayable: fight again after every match
- Built with object-oriented Python (`Player`, `Enemy` and `Weapon` classes)

## Requirements

- Python 3.6 or higher
- No external libraries (only the built-in `time` module)

## How to Run

```bash
python oop.py
```

> Replace `oop.py` with the name of your file.

## How to Play

1. Your player's stats are shown at the start of each fight.
2. Type the enemy you want to fight: `goblin`, `samurai` or `fighter`.
3. The battle runs automatically in rounds. In each round you attack first, then the enemy attacks, followed by a 3-second countdown.
4. The fight ends when you or the enemy reaches 0 health.
5. If you win, you gain levels equal to the enemy's level and can choose to heal or change weapon.
6. If you lose, it is **GAME OVER**.
7. After a win, choose whether to fight again.

## Game Details

### Player (starting stats)

| Stat   | Value |
|--------|-------|
| Health | 100   |
| Level  | 1     |
| Weapon | Stick |

### Enemies

| Enemy   | Health | Damage | Level reward |
|---------|--------|--------|--------------|
| Goblin  | 100    | 15     | 1            |
| Samurai | 100    | 25     | 5            |
| Fighter | 100    | 45     | 10           |

### Weapons

| Weapon  | Damage | Level cost | Required level |
|---------|--------|------------|----------------|
| Stick   | 20     | 1          | Starting weapon |
| Axe     | 30     | 5          | 5              |
| Machete | 40     | 10         | 10             |
| Katana  | 50     | 20         | 20             |

### Healing

- Costs **1 level** and restores **50 health**.
- Only works if your health is **50 or below**.
- Requires a level of at least 2.

### Changing Weapons

- Offered after a win once your level is 5 or higher.
- Buying a weapon deducts its cost from your levels.

## Code Structure

| Class    | Purpose |
|----------|---------|
| `Player` | Holds health, level and weapon. Handles attacking, healing, changing weapons and displaying stats. |
| `Enemy`  | Holds name, health, damage and level. Handles attacking the player. |
| `Weapon` | Holds name, damage and cost. |

The main game loop handles enemy selection, the battle rounds, rewards and replay.

## Known Issues and Ideas for Improvement

- The weapon menu opens only above level 5 (`> 5`), but the game offers it at level 5 (`>= 5`), so at exactly level 5 nothing happens.
- Entering text instead of a number in the weapon menu crashes the game.
- Player health is not restored between fights (only enemy health resets).
- Choosing the weapon you already have restarts the menu through recursion.
- Ideas: random damage and critical hits, more enemies, a save system, colored output, a defend option, and unit tests.

## License

This project is open source. Add a license of your choice (for example, MIT).

## Author

`ARPIT GUPTA`
