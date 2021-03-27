try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError :  
  print("exception in importing module in gameRules")


#Game rules : Checking dices, Winning player;
class GameRules(object):
    # def __init__(self, GameRules, controller):
    def __init__(self, *args, **kwargs):
        # self.controller = controller
        self.score = 0

    
    def n1(self, dices: list) -> int:
        print('Player choose 1')
# Number of one 
        score = 0
        for i in range(5):
            if dices[i] == 1:
                score = score + dices[i]
        return score
    
    
    def n2(self, dices: list) -> int:
        print('Player choose 2')
# Number of two 
        score = 0
        for i in range(5):
            if dices[i] == 2:
                score = score + dices[i]
        return score

    
    def n3(self, dices: list) -> int:
        print('Player choose 3')
# Number of three 
        score = 0
        for i in range(5):
            if dices[i] == 3:
                score = score + dices[i]
        return score


    def n4(self, dices: list) -> int:
        print('Player choose 4')
# Number of four 
        score = 0
        for i in range(5):
            if dices[i] == 4:
                score = score + dices[i]
        return score

        
    def n5(self, dices: list) -> int:
        print('Player choose 5')
# Number of five 
        score = 0
        for i in range(5):
            if dices[i] == 5:
                score = score + dices[i]
        return score


    def n6(self, dices: list) -> int:
        print('Player choose 6')
# Number of six 
        score = 0
        for i in range(5):
            if dices[i] == 6:
                score = score + dices[i]
        return score


    def brelan(self, dices: list) -> int:
        print('Player choose brelan')
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
        print('Player choose carre')
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
        print('Player choose full')
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
        print('Player choose petite Suite')
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
        print('Player choose grande suite')
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
        print('Player choose yam')
#Check for 5 same dices
        for i in range(1, 5):
            if dices[i] != dices[i - 1]:
                return 0
        return 50 + sum(dices)


    def chance(self, dices: list) -> int:
        print('Player choose chance')
# Sum of dices
        return sum(dices)