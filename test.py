import tkinter as tk
window = tk.Tk()
window.title("Welcome to scary adventure game")
window.geometry("700x600")
question_label = tk.Label(window, text="", wraplength=550, font=("Sans serif", 14))
question_label.pack(pady=20)
buttons = []
window.title("This is crackheads shop")
title = tk.Label(window, text="Welcome to crackheads shop", font=("Arial",16))
for i in range(8):
    button = tk.Button(window, text="", width=40, font=("Sans serif", 12))
    button.pack(pady=5)
    buttons.append(button)
buttons[0]
buttons[1]
buttons[2]
buttons[3]
buttons[4]
buttons[5]
buttons[6]
buttons[7]

# class nun_player_character():
#     def nun_player_character(self, name, reward, quest):
#         self.name = name 
#         self.reward = reward
#         self.quest = quest 
#         def name():

class hero():
<<<<<<< HEAD
    def mc(self,name,stamina,hp,attack,money):
        self.name=name
        self.stamina=stamina
        self.hp=hp
        self.attack=attack
        self.money = money
    global attack
    global stamina
    global hp
    global money
    stamina=100
    hp=100
    attack=25
    money=100
# justin = MC(100,100,100,100,100,100,3,1
    name=input("Give me a name plz")
    input(f"Here are you stats:\name:{name}\stamina:{stamina}\money:{money}\attack:{attack}\hp:{hp}")
    def potion(self,strength,health,stamina):
        self.strength=strength
        self.health=health
        self.stamina=stamina
        strength=attack*1.5
        stamina=1.5*stamina
    def health(hp,regeneration):
        hp.regeneration=regeneration
        hp.point=point
        regeneration=1
    global point
    global regeneration
    def sword_stat(self,damage):
        self.damage=damage
    
=======
    def merchant(self, money, staff, sword, scythe,armour):
        self.money = money
        self.staff = staff
        self.sword = sword
        self.scythe = scythe
        self.armour = armour
    def npc(self,reward,quest):
        self.reward = reward
        self.quest = quest
    def biome(SELF,GRASSLAND,DESERT,FOREST,WETLAND,CHINA):
        SELF.GRASSLAND = GRASSLAND
        SELF.DESERT = DESERT 
        SELF.FOREST = FOREST
        SELF.WETLAND = WETLAND
        SELF.CHINA = CHINA 
    def mini_boss(self,health, damage, drop, name):
        self.drop = drop
        self.health = health
        self.damage = damage 
        self.name = name
    def bosses(self,dumpling_warrior,Tharok_the_World_Eater,a_really_big_dog,bigfoot,sea_dragon):
        self.dumpling_warrior = dumpling_warrior
        self.Tharok_the_World_Eater = Tharok_the_World_Eater
        self.a_really_big_dog = a_really_big_dog
        self.bigfoot = bigfoot
        self.sea_dragon = sea_dragon
    def boss(self,health,damage,drop,name):
        self.health = health
        self.damage = damage
        self.drop = drop 
        self.name = name 
    def interact(merchant):
        if merchant():
            input("Welcome to arbys")
            input("\n here is what we sell")
            input(" {items}")
            
            


# window.mainloop()
>>>>>>> merchant
