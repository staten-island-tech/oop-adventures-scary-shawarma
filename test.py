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