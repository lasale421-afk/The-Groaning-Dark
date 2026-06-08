# The Groaning Dark

A terminal-based dungeon RPG written in Python. Three characters. Twenty floors. One way out.

---

## How to run

```bash
python dungeon.py
```

Requires Python 3.10+. No external dependencies — pure stdlib.

---

## Characters

**Aldric — Warrior**
High HP, high defense. Wins by outlasting enemies. Starts with a Health Potion and the Counter ability.
- Counter: halves incoming damage and hits back. 3 turn cooldown.
- Unlocks War Cry at floor 7, Last Stand at floor 13.

**Seraphel — Mage**
Low HP, high burst damage. Fireball ignores enemy defense entirely. Starts with a Mana Potion.
- Fireball: 1.6x damage, ignores defense. Costs 20 mana. 2 turn cooldown.
- Unlocks Frost Nova at floor 7, Mana Burn at floor 13.

**Vex — Rogue**
Medium HP, fast damage. Critical Strike deals double damage with a 65% chance. Starts with a Smoke Bomb.
- Critical Strike: 65% chance to deal 2x damage. 3 turn cooldown.
- Unlocks Pickpocket at floor 7, Shadow Step at floor 13.

---

## Combat

Each turn choose from:
- **[1] Attack** — standard attack, damage = ATK - enemy DEF (minimum 1)
- **[2] Item** — use something from your inventory
- **[3] Special** — use an unlocked ability (if not on cooldown)
- **[4] Descriptions** — read item and ability descriptions
- **[5] Escape** — 50% chance to flee (disabled on boss floors)

Vampires regenerate 4 HP per turn. Trolls regenerate 2 HP per turn. Both regen is suppressed if you deal more than 15% of their max HP in a single hit.

---

## Progression

- 20 floors total, 5-10 fights per floor
- Boss fights at floors 5, 10, 15, and 20 — class-specific enemies
- XP from kills and floor completion triggers level ups
- Stat gains on level up vary by class
- 30% chance a shop appears between floors
- Random events between fights: treasure, fountain, trap, or nothing

---

## Items

| Item | Effect |
|------|--------|
| Health Potion | Restore 30 HP |
| Large HP Potion | Restore 60 HP |
| Mana Potion | Restore 40 mana (mage only) |
| Smoke Bomb | Guaranteed escape from non-boss fights |
| Attack Scroll | +5 ATK permanently |
| Defense Scroll | +3 DEF permanently |
| Mana Scroll | +5 max mana (mage only) |

Story items are class-specific and appear in shops. Each can only be purchased once.

---

## Bosses

Each class faces different bosses at floors 5, 10, 15, and 20.

| Floor | Warrior | Mage | Rogue |
|-------|---------|------|-------|
| 5 | Rotlord | Flayed Archivist | Pale Huntress |
| 10 | Pale Duchess | Dreaming Colossus | Chained God |
| 15 | Brother | Mirror Mage | Warden's Shadow |
| 20 | Dungeon Heart | Thought That Eats | Warden of Nothing |

You cannot escape boss fights. The game ensures you enter each boss at minimum 60% HP.

---

## Project structure

```
dungeon.py       # everything — all game logic, combat, loop, data
README.md        # this file
```

Phase 2 (planned): Pygame visual layer. The Python logic stays untouched — a separate `game.py` will import `dungeon.py` and replace all `print()` and `input()` calls with a real game window.

---

## Story

Each character has a full written backstory that plays out through floor text, questlines, and boss encounters. Tone is dark fantasy — personal motivations, no chosen-one framing, endings that fit who each character actually is.

The dungeon is not random. It has been there longer than anyone remembers. It picks its visitors.
