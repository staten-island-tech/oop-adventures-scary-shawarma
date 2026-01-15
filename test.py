# import tkinter as tk
# window = tk.Tk()
# window.title("scary srharmma game")
# window.geometry("700x600")

# question_label = tk.Label(
#     window,
#     text="Welcome to the Crackhead's Shop!",
#     wraplength=550,
#     bg="darkslategray"
# )
# question_label.pack(pady=20)
# class Hero:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 100
#         self.stamina = 100
#         self.attack = 25
#         self.money = 100

#     def drink_potion(self):
#         if self.stamina >= 20:
#             self.stamina -= 20
#             self.hp = min(100, self.hp + 30)
#             return "You healed 30 HP!"
#         return "Not enough stamina!"

#     def buy_sword(self):
#         if self.money >= 50:
#             self.money -= 50
#             self.attack += 10
#             return "You bought a sword and got +10 ATK"
#         return "Not enough money"
# class Boss:
#     def __init__(self, name, hp, attack, reward):
#         self.name = name
#         self.hp = hp
#         self.attack = attack
#         self.reward = reward
# hero = Hero("Player")

# bosses = [
#     Boss("Dumpling Warrior", 120, 18, 75),
#     Boss("Big Dog of Doom", 160, 22, 100),
#     Boss("Tharok COSMIC World Eater", 220, 30, 200),
# ]


# def change_text(text):
#     question_label.config(text=text)
# def show_stats():
#     change_text(
#         f"Name: {hero.name}\n"
#         f"HP: {hero.hp}\n"
#         f"Stamina: {hero.stamina}\n"
#         f"Attack: {hero.attack}\n"
#         f"Money: ${hero.money}\n\n"
#         f"Bosses defeated: {boss_index}/{len(bosses)}"
#     )
# def buy_sword():
#     change_text(hero.buy_sword())
# def start_boss_fight():
#     global current_boss, in_combat
#     if boss_index >= len(bosses):
#         change_text("You have defeated ALL BOSSES!\nYou are a legend.")
#         return
#     current_boss = bosses[boss_index]
#     in_combat = True
#     change_text(
#         f"Boss {boss_index + 1}: {current_boss.name}\n\n"
#         f"HP: {current_boss.hp}"
#     )
#     combat_buttons()
# def player_attack():
#     global in_combat, boss_index
#     if not in_combat:
#         return
#     current_boss.hp -= hero.attack
#     if current_boss.hp <= 0:
#         hero.money += current_boss.reward
#         boss_index += 1
#         in_combat = False

#         change_text(
#             f"You defeated {current_boss.name}!\n"
#             f"Reward: ${current_boss.reward}"
#         )
#         shop_buttons()
#         return
#     boss_attack("You attacked the boss!")
# def boss_attack(prefix=""):
#     hero.hp -= current_boss.attack

#     if hero.hp <= 0:
#         change_text("You were defeated...\nyou lost.")
#         return

#     change_text(
#         f"{prefix}\n\n"
#         f"{current_boss.name} HP: {current_boss.hp}\n"
#         f"Your HP: {hero.hp}"
#     )
# def combat_buttons():
#     buttons[0].config(text="Attack", command=player_attack, state="normal")
#     buttons[1].config(text="Heal", command=, state="normal")
# def shop_buttons():
#     buttons[0].config(text="Show Stats", command=show_stats, state="normal")
#     buttons[1].config(text="Buy Sword ($50)", command=buy_sword, state="normal")
#     buttons[2].config(text="Fight Boss", command=start_boss_fight, state="normal")
# buttons = []
# for _ in range(8):
#     btn = tk.Button(window, width=40, font=("Sans Serif", 12))
#     btn.pack(pady=5)
#     buttons.append
# shop_buttons()
# window.mainloop()






import random
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.gold = 50
        self.has_sword = False

    def show_stats(self):
        print(f"\n{self.name}'s Stats: HP: {self.hp}, Attack: {self.attack}, Gold: {self.gold}")

class Merchant:
    def __init__(self):
        self.sword_price = 30
        self.sword_attack = 15
class Boss:
    def __init__(self):
        self.name = "Dark Overlord"
        self.hp = 120
        self.attack = 12

    def is_alive(self):
        return self.hp > 0
def fight_boss(player: Player, boss: Boss):
    print(f"\nYou encounter the {boss.name}!")
    while boss.is_alive() and player.hp > 0:
        action = input("Do you want to [A]ttack or [H]eal? ").lower()
        if action == "a":
            damage = random.randint(player.attack - 3, player.attack + 3)
            boss.hp -= damage
            print(f"You attack the {boss.name} for {damage} damage! Boss HP: {max(boss.hp, 0)}")
        elif action == "h":
            heal = random.randint(10, 20)
            player.hp += heal
            print(f"You heal yourself for {heal} HP! Your HP: {player.hp}")
        else:
            print("Invalid action!")

        if boss.hp > 0:
            boss_damage = random.randint(boss.attack - 2, boss.attack + 2)
            player.hp -= boss_damage
            print(f"The {boss.name} attacks you for {boss_damage} damage! Your HP: {max(player.hp, 0)}")

    if player.hp > 0:
        print(f"\nCongratulations! You defeated the {boss.name}!")
    else:
        print("\nYou were defeated... Game Over.")
def main():
    print("Welcome to the Adventure Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    merchant = Merchant()
    boss = Boss()

    while True:
        print("\n--- Main Menu ---")
        print("1. Visit Merchant")
        print("2. Fight Boss")
        print("3. Show Stats")
        print("4. Exit Game")
        choice = input("Choose an action: ")

        if choice == "1":
            merchant.sell_sword(player)
        elif choice == "2":
            fight_boss(player, boss)
            break
        elif choice == "3":
            player.show_stats()
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")
