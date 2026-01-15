# import tkinter as tk
# window = tk.Tk()
# window.title("Welcome to scary adventure game")
# window.geometry("700x600")
# question_label = tk.Label(window, text="", wraplength=550, font=("Sans serif", 14))
# question_label.pack(pady=20)
# window.title("This is crackheads shop")
# title = tk.Label(window, text="Welcome to crackheads shop", font=("Arial",16))
# for i in range(8):
#     button = tk.Button(window, text="", width=40, font=("Sans serif", 12))
#     button.pack(pady=5)
#     buttons.append(button)
# buttons[0]
# buttons[1]
# buttons[2]
# buttons[3]
# buttons[4]
# buttons[5]
# buttons[6]
# buttons[7]


# import tkinter as tk
# window = tk.Tk()
# window.title("Welcome to scary adventure game")
# window.geometry("700x600")
# question_label = tk.Label(window, text="", wraplength=550, font=("Sans serif", 14))
# question_label.pack(pady=20)
# buttons = []
# window.title("This is crackheads shop")
# title = tk.Label(window, text="Welcome to crackheads shop", font=("Arial",16))
# for i in range(8):
#     button = tk.Button(window, text="", width=40, font=("Sans serif", 12))
#     button.pack(pady=5)
#     buttons.append(button)
# buttons[0]
# buttons[1]
# buttons[2]
# buttons[3]
# buttons[4]
# buttons[5]
# buttons[6]
# buttons[7]
# >>>>>>> ivanc-big-sharmama'
# # class nun_player_character():
# #     def nun_player_character(self, name, lvlreq, reward, quest):
# #         self.name = name 
# #         self.lvlrq = lvlreq
# #         self.reward = reward
# #         self.quest = quest 
# #         def name():
# #             if mc self.lvlreq   


# class hero():
#     def npc(lvlrq):















class CoinGame:
    def __init__(self, player):
        self.player = player
        self.score = 0
    def flip_coin(self):
        import random
        result = random.choice(["heads", "tails"])
        print(f"{self.player} flipped {result}")
        return result
    def add_point(self, result):
        if result == "heads":
            self.score += 1
        print(f"Score: {self.score}")
game = CoinGame("Ivan")
outcome = game.flip_coin()
game.add_point(outcome)



# window.mainloop()

# window.mainloop()
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
    while enemy.hp > 0:
        self.attack(enemy)
        self.regeneration()
