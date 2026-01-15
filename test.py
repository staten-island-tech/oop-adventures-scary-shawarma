
class hero():
    def mc(self,name,stamina,max_hp,hp,attack,money):
        self.name=name
        self.stamina=stamina
        self.max_hp=max_hp
        self.hp=hp
        self.attack=attack
        self.money = money
    global attack
    global max_hp
    global stamina
    global hp
    global money
    stamina=100
    hp=100
    attack=25
    money=100
    name=input("Give me a name plz")
    print("here your stats:")
    print(f"hp:{hp}")
    print(f"stamina:{stamina}")
    print(f"attack:{attack}")
    print(f"money:{money}")
    def potion(self,strength,health,stamina):
        self.strength=strength
        self.health=health
        self.stamina=stamina
        strength=attack*1.5
        stamina=1.5*stamina
    def health(hp,regeneration):
        hp.regeneration=regeneration
        hp.point=point
        regeneration=10
    global point
    global regeneration
    def sword_stat(self,damage):
        self.damage=damage
    
    def attack(self,enemy):
        if self.stamina<= 0:
            print("Too tired")
        damage=self.attack
        self.stamina-=10
        enemy.hp-=damage
    def regen(self):
        if self.hp < self.max_hp:
            self.hp+=self.regeneration
    def statcap(self):
        self.stamina=max(0,min(100,self.stamina))
        self.hp=max(0,min(100,self.hp))
        self.money =max(0,min(100,self.money))
        self.attack=max(0,min(100,self.attack))
import random
class MC:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.stamina = 100
        self.attack = 25
        self.money = 100
    def show_stats(self):
        print(f"\n{self.name}stats")
        print(f"HP: {self.hp}")
        print(f"attack: {self.attack}")
        print(f"moneY: {self.money}")
    def drink_potion(self):
        if self.stamina >= 20:
            self.stamina -= 20
            self.hp = min(100, self.hp + 30)
            return "You healed 30 HP!"
        return "Not enough stamina!"
    def heal(self):
        if self.stamina > 20:
            self.hp += 30
            self.stamina -= 20
    def buy_sword(self):
        if self.money >= 50:
            self.money -= 50
            self.attack += 10
            return "You bought a sword and got +10 ATK"
        return "Not enough money"
    def reward(self):
        if boss_killed:
            self.money+= 60
            print("You found 60 bucks in the boss")
    def boss_killed(boss,hp):
        if boss:
            hp<0 
        print("The boss has died")
class Boss:
    def __init__(self, name, hp, attack, reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.reward = reward
bosses = [
    Boss("Dumpling Warrior", 120, 18, 75),
    Boss("Big Dog of Doom", 160, 22, 100),
    Boss("Tharok COSMIC World Eater", 220, 30, 200),
]
def boss_fight():
    global current_boss, fight
    if bosses >= len(bosses):
        print("You have defeated ALL BOSSES!\nYou are a legend.")
        return
    current_boss = bosses[boss_killed]
    
def player_attack(self, attack ):
    self.attack = attack 
    global in_combat, boss_killed
    if not in_combat:
        return
    current_boss.hp -= self.attack
    if current_boss.hp <= 0:
        reward += self.money
        boss_killed += 1
    in_combat = False
    print (f"You defeated {current_boss.name}!\n")
    print (f"Reward: ${current_boss.reward}")
    return

def boss_attack():
    MC.hp -= current_boss.attack

    if MC.hp <= 0:
        print("You were defeated...\nyou lost.")
        return
import random 
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.money = 50
    def show_stats(self):
        print(f"\n{self.name}'s Stats: HP: {self.hp}, Attack: {self.attack}, Money: {self.money}")
class Merchant:
    def __init__(self):
        self.sword_price = 30
        self.sword_attack = 15
    def is_alive(self):
        return self.hp > 0
def fight_boss(player: Player, boss: Boss):
    print(f"\nYou are fighting: {boss.name}")
    while boss.is_alive() and player.hp > 0:
        action = input("Do you want to atk or heal?").lower()
        if action == "atk":
            damage = random.randint(player.attack - 3, player.attack + 3)
            boss.hp -= damage
            print(f"You attack the{boss.name} and did this much damage:{damage}  Boss HP: {max(boss.hp, 0)}")
        elif action == "heal":
            heal = random.randint(10, 20)
            player.hp += heal
            print(f"You heal yourself by {heal} HP \nYour HP: {player.hp}")
        else:
            print("Invalid action!")
        if boss.hp > 0:
            boss_damage = random.randint(boss.attack - 2, boss.attack + 2)
            player.hp -= boss_damage
            print(f"The {boss.name} attacks you for {boss_damage} damage! Your HP: {max(player.hp, 0)}")
    if player.hp > 0:
        print(f"\nCongratulations! You defeated the {boss.name}")
    else:
        print("\nYou were defeated\nGame Over!!!!")
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
        choice = input("Choose an action: ")
        if choice == "1":
            merchant.sell_sword(player)
        elif choice == "2":
            fight_boss(player, boss)
            break
        elif choice == "3":
            player.show_stats()
        else:
            print("Invalid choice!")
