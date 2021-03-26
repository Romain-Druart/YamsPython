try:
    from gameUI import GamePage, label_player1_one, label_player1_two, label_player1_three, label_player1_four, label_player1_five, label_player1_six, label_player1_top_sub_total, label_player1_bonus, label_player1_brelan, label_player1_carre, label_player1_full, label_player1_small_suite, label_player1_great_suite, label_player1_yams, label_player1_chance, label_player1_sub_total, label_player1_total
    from gameUI import label_player2_one, label_player2_two, label_player2_three, label_player2_four, label_player2_five, label_player2_six, label_player2_top_sub_total, label_player2_bonus, label_player2_brelan, label_player2_carre, label_player2_full, label_player2_small_suite, label_player2_great_suite, label_player2_yams, label_player2_chance, label_player2_sub_total, label_player2_total
    import tkinter as tk
    from tkinter import messagebox
    from dices import validateDices, shuffleDices, dicesNumbers, getDices
except ImportError :  
  print("exception in importing module")


#Game rules : Checking dices, Winning player;
class GameRules():
    def __init__(self, GameRules, controller):
        self.controller = controller
        self.GameRules = GameRules
        self.GamePage = GamePage
        self.score = 0

        self.checkOne = False; self.checkTwo = False; self.checkThree = False; self.checkFour = False; self.checkFive = False; self.checkSix = False
        self.checkBrelan = False; self.checkCarre = False; self.checkFull = False; self.checkPetiteSuite = False; self.checkGrandeSuite = False
        self.checkYams = False; self.checkChance = False

    def ReturnScore(self, combine):
        combine = validateDices()
        dices = getDices() 
        if combine == "1":
            if self.checkOne == "False":
                if 1 not in dices:
                    confirmBox = tk.messagebox.askquestion("Confirmation", "Vous avez choisi : 1 = 0 points")
                    if confirmBox == 'yes':
                        label_player1_one.config(text=self.n1(dices))
                        label_player1_total.config(text=self.n1(dices))
                else:
                    confirmBox = tk.messagebox.askquestion("Confirmation", "Vous avez choisi : 1")
                    if confirmBox == 'yes':
                        label_player1_one.config(text=self.n1(dices))
                        self.checkOne = True
            else:
                tk.messagebox.showerror("Alerte", "Vous avez déjà joué les 1")


        elif combine == "2":
            score = self.n1(dices)
        elif combine == "3":
            score = self.n1(dices)
        elif combine == "4":
            score = self.n1(dices)
        elif combine == "5":
            score = self.n1(dices)
        elif combine == "6":
            score = self.n1(dices)
        elif combine == "Brelan":
            score = self.n1(dices)
        elif combine == "Carré":
            score = self.n1(dices)
        elif combine == "Full":
            score = self.n1(dices)
        elif combine == "Petite Suite":
            score = self.n1(dices)
        elif combine == "Grande Suite":
            score = self.n1(dices)
        elif combine == "Yam":
            score = self.n1(dices)
        elif combine == "Chance":
            score = self.n1(dices)
        else:
            tk.messagebox.showinfo(title="Alert", message="Please choose a valide option")
            #throw alert
        return score

    def n1(self, dices: list) -> int:
        print('Player choose 1')
# Number of one 
        score = 0
        for i in range(5):
            if dices[i] == 1:
                score = score + dices[i]
        return score
    
    
    def n2(self, dices: list) -> int:
# Number of two 
        score = 0
        for i in range(5):
            if dices[i] == 2:
                score = score + dices[i]
        return score

    
    def n3(self, dices: list) -> int:
# Number of three 
        score = 0
        for i in range(5):
            if dices[i] == 3:
                score = score + dices[i]
        return score


    def n4(self, dices: list) -> int:
# Number of four 
        score = 0
        for i in range(5):
            if dices[i] == 4:
                score = score + dices[i]
        return score

        
    def n5(self, dices: list) -> int:
# Number of five 
        score = 0
        for i in range(5):
            if dices[i] == 5:
                score = score + dices[i]
        return score


    def n6(self, dices: list) -> int:
# Number of six 
        score = 0
        for i in range(5):
            if dices[i] == 6:
                score = score + dices[i]
        return score


    def brelan(self, dices: list) -> int:
# Check for three-of-a-kind 
        sorted_dices = sorted(dices)
        count = 1
        for i in range(1, 5):
            if sorted_dices[i] == sorted_dices[i - 1]:
                count = count + 1
            else:
                count = 1
            if count == 3:
                return sum(dices)
        return 0

    
    def carre(self, dices: list) -> int:
# Check for four-of-a-kind 
        sorted_dices = sorted(dices)
        count = 1
        for i in range(1, 5):
            if sorted_dices[i] == sorted_dices[i - 1]:
                count = count + 1
            else:
                count = 1
            if count == 4:
                return 40 + sum(dices)
        return 0


    def full(self, dices: list) -> int:
#Check for full
        sorted_dices = sorted(dices)
        count = 1
        two, three = False, False
        for i in range(1, 5):
            if sorted_dices[i] == sorted_dices[i - 1]:
                count = count + 1
            else:
                count = 1
            if count == 2:
                two = True
            if count == 3:
                three = True
        if two and three:
            return 25 + sum(dices)
        return 0
    
    
    def petiteSuite(self, dices: list) -> int:
#Check for sequences of length 4
        sorted_dices = sorted(dices)
        count = 1
        for i in range(1, 5):
            if sorted_dices[i] == sorted_dices[i - 1] + 1:
                count = count + 1
            elif sorted_dices[i] != sorted_dices[i - 1]:
                count = 1
            if count == 4:
                return 30
        return 0

    
    def grandeSuite(self, dices: list) -> int:
#Check for sequences of length 5
        sorted_dices = sorted(dices)
        count = 1
        for i in range(1, 5):
            if sorted_dices[i] == sorted_dices[i - 1] + 1:
                count = count + 1
            elif sorted_dices[i] != sorted_dices[i - 1]:
                count = 1
            if count == 5:
                return 40
        return 0


    def yams(self, dices: list) -> int:
#Check for 5 same dices
        for i in range(1, 5):
            if dices[i] != dices[i - 1]:
                return 0
        return 50 + sum(dices)


    def chance(self, dices: list) -> int:
# Sum of dices
        return sum(dices)