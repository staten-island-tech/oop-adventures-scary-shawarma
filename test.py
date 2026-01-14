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
