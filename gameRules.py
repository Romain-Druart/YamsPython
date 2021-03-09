#Game rules : Checking dices, Winning player;
class GameRules():


    def n1(dices: list) -> int:
# Number of one 
        score = 0
        for i in range(5):
            if dices[i] == 1:
                score = score + dices[i]
        return score
     
 
    def n2(dices: list) -> int:
        # Number of two 
        score = 0
        for i in range(5):
            if dices[i] == 2:
                score = score + dices[i]
        return score
     
 
    def n3(dices: list) -> int:
        # Number of three 
        score = 0
        for i in range(5):
            if dices[i] == 3:
                score = score + dices[i]
        return score
     
 
    def n4(dices: list) -> int:
        # Number of four 
        score = 0
        for i in range(5):
            if dices[i] == 4:
                score = score + dices[i]
        return score
     
 
    def n5(dices: list) -> int:
        # Number of five 
        score = 0
        for i in range(5):
            if dices[i] == 5:
                score = score + dices[i]
        return score
     
 
    def n6(dices: list) -> int:
        # Number of six 
        score = 0
        for i in range(5):
            if dices[i] == 6:
                score = score + dices[i]
        return score
     
 
    def brelan(dices: list) -> int:
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
 
 
    def carre(dices: list) -> int:
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
 
 
    def full(dices: list) -> int:
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
 
 
    def petiteSuite(dices: list) -> int:
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
 
 
    def grandeSuite(dices: list) -> int:
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
 
 
    def yams(dices: list) -> int:
        #Check for 5 same dices
        for i in range(1, 5):
            if dices[i] != dices[i - 1]:
                return 0
 
        return 50 + sum(dices)
 
 
    def chance(dices: list) -> int:
        # Sum of dices
        return sum(dices)