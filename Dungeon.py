import random 
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

absorb_messages = {
    "warrior": "attacks but your armor absorbs it completely.",
    "mage":    "strikes but your ward deflects the blow.",
    "rogue":   "swings and misses — you were already gone.",
}
DESCRIPTIONS = {
    "Health Potion":        "Restores 30 HP.",
    "Large HP Potion":      "Restores 60 HP.",
    "Mana Potion":          "Restores 50 mana.",
    "Smoke Bomb":           "Guaranteed escape from any fight.",
    "Attack Scroll":        "Permanently increases ATK by 5.",
    "Defense Scroll":       "Permanently increases DEF by 3.",
    "Cracked Iron Pauldron":"A battered shoulder guard. +2 DEF.",
    "Pale Duchess Ring":    "Smells of old perfume. +5 ATK.",
    "Tome of Hunger":       "Pages filled with hunger. +8 max mana.",
    "Warden's Cloak":       "Reduces enemy detection range. +4 DEF.",
    "counter":      "Halves incoming damage for this turn.And deals 20% more damage 3 turn cooldown.",
    "warcry":     "+5 ATK for 3 turns. 4 turn cooldown.",
    "laststand":  "Triple damage when HP is below 30%. 5 turn cooldown.",
    "fireball":   "Double damage, ignores defense. Costs 20 mana. 2 turn cooldown.",
    "frostnova":  "Enemy skips their next attack. Costs 30 mana. 4 turn cooldown.",
    "manaburn":   "Convert 20 HP into 40 mana. No cooldown.",
    "crit":       "40% chance to deal double damage. 3 turn cooldown.",
    "pickpocket": "Steal 10-30 gold mid combat. 3 turn cooldown.",
    "shadowstep": "Guaranteed dodge on the next attack. 4 turn cooldown."
}
ENEMY_XP = {
    "Goblin": 20, "Orc": 35, "Skeleton": 25,
    "Troll": 50, "Vampire": 45,
    "Rotlord": 150, "Pale Duchess": 200, 
    "Brother": 300, "Dungeon Heart": 500,
    "Flayed Archivist": 150, "Dreaming Colossus": 200,
    "Mirror Mage": 300, "Thought That Eats": 500,
    "Pale Huntress": 150, "Chained God": 200, 
    "Warden's Shadow": 300, "Warden of Nothing": 500
}

BOSSES = {
    "warrior": {
        5:  {"name": "Rotlord",       "hp": 240, "max_hp": 240, "atk": 40, "defense": 17, "gold": 140},
        10: {"name": "Pale Duchess",  "hp": 400, "max_hp": 400, "atk": 55, "defense": 30, "gold": 400},
        15: {"name": "Brother",       "hp": 320, "max_hp": 320, "atk": 48, "defense": 20, "gold": 280},
        20: {"name": "Dungeon Heart", "hp": 500, "max_hp": 500, "atk": 65, "defense": 35, "gold": 600},
    },
    "mage": {
        5:  {"name": "Flayed Archivist",  "hp": 200, "max_hp": 200, "atk": 35, "defense": 12, "gold": 140},
        10: {"name": "Dreaming Colossus", "hp": 450, "max_hp": 450, "atk": 58, "defense": 35, "gold": 400},
        15: {"name": "Mirror Mage",       "hp": 300, "max_hp": 300, "atk": 50, "defense": 22, "gold": 280},
        20: {"name": "Thought That Eats", "hp": 480, "max_hp": 480, "atk": 62, "defense": 30, "gold": 600},
    },
    "rogue": {
        5:  {"name": "Pale Huntress",     "hp": 220, "max_hp": 220, "atk": 38, "defense": 15, "gold": 140},
        10: {"name": "Chained God",       "hp": 420, "max_hp": 420, "atk": 56, "defense": 28, "gold": 400},
        15: {"name": "Warden's Shadow",   "hp": 310, "max_hp": 310, "atk": 48, "defense": 21, "gold": 280},
        20: {"name": "Warden of Nothing", "hp": 490, "max_hp": 490, "atk": 63, "defense": 33, "gold": 600},
    }
}

items_pool = {
    "warrior": [
        {"name": "Health Potion",   "type": "heal",    "value": 30, "price": 40},
        {"name": "Large HP Potion", "type": "heal",    "value": 60, "price": 80},
        {"name": "Smoke Bomb",      "type": "escape",  "value": 1,  "price": 60},
        {"name": "Attack Scroll",   "type": "atk",     "value": 5,  "price": 100},
        {"name": "Defense Scroll",  "type": "defense", "value": 3,  "price": 90},
    ],
    "mage": [
        {"name": "Health Potion",   "type": "heal",    "value": 30, "price": 40},
        {"name": "Mana Potion",     "type": "mana",    "value": 50, "price": 45},
        {"name": "Smoke Bomb",      "type": "escape",  "value": 1,  "price": 60},
        {"name": "Attack Scroll",   "type": "atk",     "value": 5,  "price": 100},
        {"name": "Mana Scroll",     "type": "upgrade", "value": 5,  "price": 100},
    ],
    "rogue": [
        {"name": "Health Potion",   "type": "heal",    "value": 30, "price": 40},
        {"name": "Large HP Potion", "type": "heal",    "value": 60, "price": 80},
        {"name": "Smoke Bomb",      "type": "escape",  "value": 1,  "price": 60},
        {"name": "Attack Scroll",   "type": "atk",     "value": 5,  "price": 100},
        {"name": "Defense Scroll",  "type": "defense", "value": 3,  "price": 90},
    ],
}

story_items_pool = {
    "warrior": [
        {"name": "Cracked Iron Pauldron", "type": "defense", "value": 2, "price": 55},
        {"name": "Pale Duchess Ring",     "type": "atk",     "value": 5, "price": 120},
    ],
    "mage" : [
        {"name": "Tome of Hunger", "type": "mana", "value": 8 , "price": 70},
    ],
    "rogue" : [
        {"name": "Warden's Cloak", "type" : "defense", "value": 4 , "price": 85},
    ]
}

victory_lines = {
    "warrior": "He sat on a rock outside the entrance and counted the coins until the sun was high and warm on his ruined back.",
    "mage":    "She wrote beneath it: I have questions.",
    "rogue":   "Felt right. Didn't need to know why."
}

game_over_lines = {
    "warrior": "The shield held longer than the man behind it.",
    "mage":    "The equation had one variable she failed to account for.",
    "rogue":   "Forty percent. It just wasn't that turn."
}


def create_character():
    print('Character available: mage, warrior , rogue. Their stats ? Surprise!!')
    while True:
        answer = str(input("choose your character: ")).strip().lower()
        
        if answer not in ["warrior", "mage", "rogue"]:
            print("try choosing one of these options: mage, rogue, warrior")
        if answer =="warrior":
            name = input("enter your name: ")
            return  { "name": name,
                "class": "warrior",
                "hp": 160, "max_hp": 160,
                "atk": 14, "defense": 10,
                "mana": 0, "max_mana": 0,
                "level": 1, "floor": 1,
                "gold": 0, "fights_won": 0,
                "ability": "counter", "cooldown": 0,
                "xp": 0, "xp_to_next": 100,
                "purchased_story_items": [],
                "inventory": [{"name": "Health Potion", "type": "heal", "value": 30}]
            }
        elif answer == "mage":
            name = input("enter your name: ")
            return {
                "name": name,
                "class": "mage",
                "hp": 90, "max_hp": 90,
                "atk": 25, "defense": 6,
                "mana": 90, "max_mana": 90,
                "level": 1, "floor": 1,
                "gold": 0, "fights_won": 0,
                "ability": "fireball", "cooldown":0,
                "xp": 0, "xp_to_next": 100,
                "purchased_story_items": [],
                "inventory": [{"name": "Mana Potion", "type": "mana", "value": 50}]
            }
        elif answer == "rogue":
            name = input("enter your name: ")
            return {
                "name": name,
                "class": "rogue",
                "hp": 120, "max_hp": 120,
                "atk": 23, "defense": 7,
                "mana": 0, "max_mana": 0,
                "level": 1, "floor": 1,
                "gold": 0, "fights_won": 0,
                "ability": "critical strike", "cooldown": 0,
                "xp": 0, "xp_to_next": 100,
                "purchased_story_items": [],
                "inventory": [{"name": "Smoke Bomb", "type": "escape", "value": 1}]
            }
        else:
            print("choose warrior, mage or rogue")

def generate_enemies(floor, player_class):
    enemies = [
        {"name": "Goblin",   "hp": 30,  "max_hp": 30, "atk": 8,  "defense": 2,  "gold": 5},
        {"name": "Orc",      "hp": 65,  "max_hp": 65, "atk": 14, "defense": 5,  "gold": 10},
        {"name": "Skeleton", "hp": 40,  "max_hp": 40, "atk": 12, "defense": 3,  "gold": 8},
        {"name": "Troll",    "hp": 95,  "max_hp": 95, "atk": 16, "defense": 8,  "gold": 15},
        {"name": "Vampire",  "hp": 60,  "max_hp": 60, "atk": 18, "defense": 7,  "gold": 20},
    ]
    if floor in [5, 10, 15, 20]:
        return BOSSES[player_class][floor]
    else:
        enemy = random.choice(enemies)
        scale = 1 + (floor-1) * 0.2
        return {
            "name": enemy["name"],
            "hp": int(enemy["hp"] * scale),
            "max_hp": int(enemy["max_hp"] * scale),
            "atk": int(enemy["atk"] * scale),
            "defense": int(enemy["defense"] * scale),
            "gold": int(enemy["gold"] * scale)
        }

def enemy_regen(enemy, damage_dealt):
    if damage_dealt > enemy['max_hp'] * 0.15:
        return
    if enemy['name'] == "Vampire" and enemy['hp'] < enemy['max_hp']:
        enemy['hp'] = min(enemy['hp'] + 4, enemy['max_hp'])
    if enemy['name'] == "Troll" and enemy['hp'] < enemy['max_hp']:
        enemy['hp'] = min(enemy['hp'] + 2, enemy['max_hp'])

def combat(player, enemy):
    boss_names = [
        "Rotlord", "Pale Duchess", "Brother", "Dungeon Heart",
        "Flayed Archivist", "Dreaming Colossus", "Mirror Mage", "Thought That Eats",
        "Pale Huntress", "Chained God", "Warden's Shadow", "Warden of Nothing"
    ]
    is_boss = enemy['name'] in boss_names
    while True: 
        
        abilities = []
        if player["class"] == "warrior":
            abilities.append({"name": "Counter (1/2 dmg for 1 turn)", "key": "counter", "cd": 3})
            if player["floor"] >= 7:
                abilities.append({"name": "War Cry (+5 ATK for 3 turns)", "key": "warcry", "cd": 4})
            if player["floor"] >= 13:
                abilities.append({"name": "Last Stand (triple dmg when HP < 30%)", "key": "laststand", "cd": 5})
        elif player["class"] == "mage":
            abilities.append({"name": "Fireball (20 mana, double dmg)", "key": "fireball", "cd": 2})
            if player["floor"] >= 7:
                abilities.append({"name": "Frost Nova (skip enemy turn, 30 mana)", "key": "frostnova", "cd": 4})
            if player["floor"] >= 13:
                abilities.append({"name": "Mana Burn (20 HP -> 40 mana)", "key": "manaburn", "cd": 0})
        elif player["class"] == "rogue":
            abilities.append({"name": "Critical Strike (40% double dmg)", "key": "crit", "cd": 3})
            if player["floor"] >= 7:
                abilities.append({"name": "Pickpocket (steal 10-30 gold)", "key": "pickpocket", "cd": 3})
            if player["floor"] >= 13:
                abilities.append({"name": "Shadow Step (dodge next attack)", "key": "shadowstep", "cd": 4})

        clear()
        if player["cooldown"] > 0:
            print(f"ability on cooldown - {player['cooldown']} turns remaining")
        if player["class"] == "mage":
            print(f"\n {player['name']} HP: {player['hp']}/{player['max_hp']} Mana: {player['mana']}/{player['max_mana']}")
        else:
            print(f"\n {player['name']} HP: {player['hp']}/{player['max_hp']}")
        print(f"\n {enemy['name']} HP: {enemy['hp']}/{enemy['max_hp']}")
        print(f"[1] attack")
        print(f"[2] item")
        print(f"[3] special")
        print(f"[4] descriptions")
        if not is_boss:
            print(f"[5] escape")
        try:    
            choice = int(input("what do you want to do? "))

            if choice == 1:
                damage = max(5, player["atk"] - enemy["defense"])
                enemy["hp"] -= damage
                if enemy["hp"] <= 0:
                    return 'you won'
                enemy_regen(enemy, damage)
                get_attacked = max(0, enemy["atk"] - player["defense"])
                if get_attacked == 0:
                    print(f"{enemy['name']} {absorb_messages[player["class"]]}")
                player["hp"] -= get_attacked
                if player["cooldown"] > 0:
                    player["cooldown"] -= 1
                if player["hp"] <= 0:
                    return 'you lost'

            elif choice == 2:
                if len(player["inventory"]) == 0:
                    print("your inventory is empty!")
                    continue
                try:
                    for i, item in enumerate(player["inventory"]):
                        print(f"[{i}] {item['name']}")
                    print(f"[{len(player['inventory'])}] go back")
                    pick = int(input("choose an item: "))
                    if pick == len(player['inventory']):
                        continue
                    item = player["inventory"][pick]
                    if item["type"] == "heal":
                        player["hp"] += item["value"]
                        if player["hp"] > player["max_hp"]:
                            player["hp"] = player["max_hp"]
                        print(f"you healed {item['value']} HP")
                        player["inventory"].pop(pick)
                        get_attacked = max(0, enemy["atk"] - player["defense"])
                        enemy_regen(enemy, 0)
                        player["hp"] -= get_attacked
                        if player["cooldown"] > 0:
                            player["cooldown"] -= 1
                        if player["hp"] <= 0:
                            return 'you lost'
                    elif item["type"] == "mana":
                        player["mana"] += item["value"]
                        if player["mana"] > player["max_mana"]:
                            player["mana"] = player["max_mana"]
                        player["inventory"].pop(pick)
                        get_attacked = max(0, enemy["atk"] - player["defense"])
                        enemy_regen(enemy, 0)
                        player["hp"] -= get_attacked
                        if player["cooldown"] > 0:
                            player["cooldown"] -= 1
                        if player["hp"] <= 0:
                            return 'you lost'
                    elif item["type"] == "atk":
                        player["atk"] += item["value"]
                        player["inventory"].pop(pick)
                        get_attacked = max(0, enemy["atk"] - player["defense"])
                        enemy_regen(enemy, 0)
                        player["hp"] -= get_attacked
                        if player["cooldown"] > 0:
                            player["cooldown"] -= 1
                        if player["hp"] <= 0:
                            return 'you lost'
                    elif item["type"] == "defense":
                        player["defense"] += item["value"]
                        player["inventory"].pop(pick)
                        get_attacked = max(0, enemy["atk"] - player["defense"])
                        enemy_regen(enemy, 0)
                        player["hp"] -= get_attacked
                        if player["cooldown"] > 0:
                            player["cooldown"] -= 1
                        if player["hp"] <= 0:
                            return 'you lost'

                    elif item["type"] == "upgrade":
                        player["mana"] += item["value"]
                        player["inventory"].pop(pick)
                        get_attacked = max(0, enemy["atk"] - player["defense"])
                        enemy_regen(enemy, 0)
                        player["hp"] -= get_attacked
                        if player["cooldown"] > 0:
                            player["cooldown"] -= 1
                        if player["hp"] <= 0:
                            return 'you lost'

                    elif item["type"] == "escape":
                        if is_boss:
                            print("there is no escape from this fight.")
                            input("\npress enter to continue...")
                        else:
                            player["inventory"].pop(pick)
                            return 'escaped'
                except ValueError:
                    print("this value is weird, try again")

            elif choice == 3:
                if player["cooldown"] > 0:
                    print(f"ability on cooldown - {player['cooldown']} turns remaining")
                else:
                    for i, ability in enumerate(abilities):
                        print(f"[{i}] {ability['name']}")
                    print(f"[{len(abilities)}] back")
                    try:
                        pick = int(input("choose an ability: "))
                        if pick == len(abilities):
                            continue
                        elif 0 <= pick < len(abilities):
                            chosen = abilities[pick]["key"]

                            if chosen == "counter":
                                print("you are ready to counter")
                                player["cooldown"] = 3
                                get_attacked = max(0, enemy["atk"] - player["defense"])
                                player["hp"] -= (get_attacked // 2)
                                damage = max(5, player["atk"] - enemy["defense"])
                                enemy["hp"] -= damage
                                if enemy['hp'] <= 0:
                                    return 'you won'
                                enemy_regen(enemy, damage)
                                if player["cooldown"] > 0:
                                    player["cooldown"] -= 1
                                if player["hp"] <= 0:
                                    return 'you lost'

                            elif chosen == "fireball":
                                if player["mana"] >= 20:
                                    damage_fireball = player["atk"] * 1.6
                                    enemy["hp"] -= damage_fireball
                                    player["mana"] -= 20
                                    player["cooldown"] = 2
                                    enemy_regen(enemy, damage_fireball)
                                    if enemy["hp"] <= 0:
                                        return 'you won'
                                    get_attacked = max(0, enemy["atk"] - player["defense"])
                                    player["hp"] -= get_attacked
                                    if player["cooldown"] > 0:
                                        player["cooldown"] -= 1
                                    if player["hp"] <= 0:
                                        return 'you lost'
                                else:
                                    print("you don't have enough mana")

                            elif chosen == "crit":
                                chance = round(random.random(), 1)
                                if chance > 0.35: #was 0.4 , buffed . crits more often now
                                    damage_strike = player["atk"] * 2
                                    enemy["hp"] -= damage_strike
                                    enemy_regen(enemy, damage_strike)
                                    print("critical hit!")
                                else:
                                    damage_miss = max(5, player["atk"] - enemy["defense"])
                                    enemy["hp"] -= damage_miss
                                    enemy_regen(enemy, damage_miss)
                                    print("missed the crit, normal damage.")
                                if enemy["hp"] <= 0:
                                    return 'you won'
                                get_attacked = max(0, enemy["atk"] - player["defense"])
                                player["hp"] -= get_attacked
                                if player["hp"] <= 0:
                                    return 'you lost'
                                player["cooldown"] = 3

                            elif chosen == "warcry":
                                print("war cry coming soon")
                            elif chosen == "frostnova":
                                print("frost nova coming soon")
                            elif chosen == "pickpocket":
                                print("pickpocket coming soon")
                            elif chosen == "laststand":
                                print("last stand coming soon")
                            elif chosen == "manaburn":
                                print("mana burn coming soon")
                            elif chosen == "shadowstep":
                                print("shadow step coming soon")
                        else:
                            print("choose one of the options.")
                    except ValueError:
                        print("this value is weird, try again")

            elif choice == 4:
                print("\n--- INVENTORY ---")
                for item in player["inventory"]:
                    desc = DESCRIPTIONS.get(item["name"], "no description available.")
                    print(f"{item['name']}: {desc}")
                print("\n--- ABILITIES ---")
                for ability in abilities:
                    desc = DESCRIPTIONS.get(ability["key"], "no description available.")
                    print(f"{ability['name']}: {desc}")
                input('\npress enter to continue...')

            elif choice == 5:
                if is_boss:
                    print("you can't escape a boss fight.")
                else:
                    chance = round(random.random(), 1)
                    if chance > 0.5:
                        return 'escaped'
                    else:
                        print('lost your 50/50')
                        print('sadly, you failed to escape and got attacked.')
                        get_attacked = max(0, enemy["atk"] - player["defense"])
                        enemy_regen(enemy, 0)
                        player["hp"] -= get_attacked 
                        if player["hp"] <= 0:
                            return 'you lost'
            else:
                print("choose 1 of those options")
        except ValueError:
            print('choose 1 of those options')

def check_levelup(player):
    if player["xp"] >= player["xp_to_next"]:
        player["level"] += 1 
        player["xp"] -= player["xp_to_next"]          # carry over leftover XP
        player["xp_to_next"] = int(100 * (player["level"] ** 1.5))  # new threshold
        if player["class"] == "warrior": 
            player["max_hp"] += 12 
            player["defense"] += 1
            player["atk"] += 2
            print(
                f"you level up, you're now level {player['level']}, here are your stats: \n"
                f"{player['name']}: "
                f"HP : {player['hp']}/{player['max_hp']} \n"    
                f"Defense: {player['defense']} \n"
                f"ATK : {player['atk']}"
            )
            input('\npress enter to continue...')
        elif player["class"] == "mage":
            player["max_hp"] += 5
            player["atk"] += 3
            player["max_mana"] += 15
            print(
                f"you level up, you're now level {player['level']}, here are your stats: \n"
                f"{player['name']}: "
                f"HP : {player['hp']}/{player['max_hp']} \n"    
                f"Mana : {player['mana']}/{player['max_mana']} \n"
                f"ATK : {player['atk']}"
            )
            input('\npress enter to continue...')
        elif player["class"] == "rogue":
            player["max_hp"] += 8
            player["atk"] += 3
            player["defense"] += 1
            print(
                f"you level up, you're now level {player['level']}, here are your stats: \n"
                f"{player['name']}: "
                f"HP : {player['hp']}/{player['max_hp']} \n"    
                f"Defense: {player['defense']} \n"
                f"ATK : {player['atk']}"
            )
            input('\npress enter to continue...')

def give_xp(player, xp_amount):
    player["xp"] += xp_amount
    print(
        f"you gained {xp_amount} xp \n "
        f"{player['xp']}/{player['xp_to_next']}"
    )
    check_levelup(player)

def loot_floor(player, floor):
    chance = round(random.random(),1)
    if chance <= 0.3: 
        obj = random.choice(items_pool[player['class']])
        if len(player["inventory"]) >= 5:
            print(f"your inventory is full, you leave {obj['name']} behind.")
        else: 
            player["inventory"].append(obj)
            print(f"you just picked a {obj['name']} !!")
            return obj
    return None 

def floor_event(player):
    chance = round(random.random(), 1)
    if chance < 0.25 : #25% chance 
        gold_amount = random.randint(10,40)
        player["gold"] += gold_amount
        print(
            f"you found a treasure!! yay \n "
            f"you found {gold_amount} gold in the treasure!\n"
            f"\n{player['name']} : {player['gold']} gold"
        )
        input('\npress enter to continue...')
    elif chance <= 0.45: #0.25 + 0.20, so 20% chance
        heal_amount = random.randint(10,20)
        player['hp'] += heal_amount 
        if player['hp'] > player['max_hp']: 
            player['hp'] = player['max_hp']
        print(
            f"you found a fountain, you heal {heal_amount} hp\n"
            f"{player['name']} : {player['hp']}/{player['max_hp']}\n"
            )
        input('\npress enter to continue...')

    elif chance <= 0.64: # 0.45 + 19 , so 19% chance
        trap_dmg = random.randint(9,15)
        player['hp'] -= trap_dmg
        print(
            f"you got hit by a trap... -{trap_dmg} hp "
            f"{player['name']} : {player['hp']}/{player['max_hp']}"
        )
        if player["hp"] <= 0:
            return 'You died'
        input('\npress enter to continue...')
    else: 
        print("you move through the corridor. nothing happens.")

def shop(player):
    # build shop stock
    clear()
    shop_items = [random.choice(items_pool[player['class']]) for _ in range(3)]
    
    # add story item if player hasn't bought it yet
    owned_names = [item['name'] for item in player['inventory']]
    available_story = [item for item in story_items_pool[player['class']] 
                   if item['name'] not in player['purchased_story_items']]
    if available_story:
        shop_items.append(random.choice(available_story))
    
    while True:
        print(f"\nyou have {player['gold']} gold.")
        for i, item in enumerate(shop_items):
            print(f"[{i}] {item['name']} - {item['price']}g")
        print(f"[{len(shop_items)}] leave")
        
        try:
            choice = int(input("what do you want to buy? "))
            
            if choice == len(shop_items):
                print("you leave the shop.")
                return
            elif 0 <= choice < len(shop_items):
                item = shop_items[choice]
                if player['gold'] < item['price']:
                    print("you don't have enough gold.")
                elif len(player['inventory']) >= 5:
                    print("your inventory is full.")
                else:
                    player['gold'] -= item['price']
                    player['inventory'].append(item)
                    if item in story_items_pool[player['class']]:
                        player['purchased_story_items'].append(item['name'])
                    print(f"you bought {item['name']}.")
                    input('\npress enter to continue...')
            else:
                print("choose one of the options.")
        except ValueError:
            print("this value is weird, try again")

def game_over(player):
    print(game_over_lines[player["class"]])
    print(f"  Floor reached : {player['floor']}")
    print(f"  Level         : {player['level']}")
    print(f"  Gold collected: {player['gold']}")
    print(f"  Kills         : {player['fights_won']}")
    input('\npress enter to continue...')
    
def victory(player):
    print(f"\n{victory_lines[player['class']]}\n")
    print(f"  Floor reached : {player['floor']}")
    print(f"  Level         : {player['level']}")
    print(f"  Gold collected: {player['gold']}")
    print(f"  Kills         : {player['fights_won']}")
    input('\npress enter to continue...')

def game_loop(player):
    for floor in range(1, 21):
        clear()
        if floor in [5, 10, 15, 20]:
            player['hp'] = max(player['hp'], int(player['max_hp'] * 0.6))
            print(f"\nyou take a breath before the door. ({player['hp']}/{player['max_hp']} HP)")
            input("\npress enter to continue...")
            enemy = generate_enemies(floor, player['class'])  # generate_enemies already handles floors 5 and 10
            print(f"\n*** BOSS FLOOR {floor} ***")
            result = combat(player, enemy)
            if result == 'you lost':
                game_over(player)
                return
            player['gold'] += enemy['gold']
            xp_amount = int(ENEMY_XP[enemy['name']] * (1 + floor * 0.1))
            give_xp(player, xp_amount)
            player['fights_won'] += 1
            input('\npress enter to continue...')
            continue  

        player['floor'] = floor
        print(f"\n You're on floor {player['floor']}. ")

        nmb_of_fight= random.randint(5,10) #number of fight per floor

        for _ in range(nmb_of_fight):
            enemy = generate_enemies(floor, player['class'])
            result = combat(player, enemy)

            if result == 'you lost':
                game_over(player)
                return 'try again'
            elif result == 'you won':
                clear()
                player['gold'] += enemy['gold']
                xp_amount = int(ENEMY_XP[enemy['name']] * (1 + floor * 0.1))
                give_xp(player, xp_amount)
                player['fights_won'] += 1
                dropped = loot_floor(player, floor)
                if dropped:
                    print(f"you killed {enemy['name']} and found a {dropped['name']}!")
                input('\npress enter to continue...')

            event_result = floor_event(player)
            if event_result == 'You died':
                clear()
                game_over(player)
                input('\npress enter to continue...')
                return
            

        #when floor cleared
        give_xp(player, player['floor'] * 30) #for floor completion
        input('\npress enter to continue...')
        player['floor'] += 1

        #30% chance shop appearence 
        chance = round(random.random(),1)
        if chance < 0.3 :
            shop(player)
    #20floors done
    victory(player)


player = create_character()
game_loop(player)