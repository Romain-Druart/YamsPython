try:
    import random
except ImportError :  
  print("exception in importing module in Dices")


class Dice(object):


    def __init__(self, *args, **kwargs):
        self.dicesNumbers = [0,0,0,0,0]
        self.dicesUI = [0,0,0,0,0]
        #self.shuffleDices(self.dicesUI)
        print(self.dicesNumbers)

    # def shuffleDices(self, dices):
    #     for i in range(len(self.dicesNumbers)):
    #         if (self.PageGame.checkDiceOne.get()==0):
    #             dices[0]= random.randint(1, 6)
    #             #change dice value
    #         elif (self.PageGame.checkDiceTwo.get()==0):
    #             dices[1]= random.randint(1, 6)
    #             #cahnge dice value
    #         elif (self.PageGame.checkDiceThree.get()==0):
    #             dices[2]= random.randint(1, 6)
    #             #cahnge dice value
    #         elif (self.PageGame.checkDiceFour.get()==0):
    #             dices[3]= random.randint(1, 6)
    #             #cahnge dice value
    #         elif (self.PageGame.checkDiceFive.get()==0):
    #             dices[4]= random.randint(1, 6)
    #             #cahnge dice value
    #         # dices[i]= random.randint(1, 6)
    #     self.dicesNumbers = dices
    #     self.displayDices(self.dicesNumbers)
    #     self.getDicesUI()           
    #     return self.dicesNumbers

    def displayDices(self, dices):
        # print("Passage dans fonction displayDices \n")
        for i in range(len(self.dicesNumbers)):
            # print("dans le for de display ")
            print(dices[i])
            if str(self.dicesNumbers[i]) in 'de1':
                dices[i] = './assets/dices/de1.png'
            elif str(self.dicesNumbers[i]) in 'de2':
                dices[i] = './assets/dices/de2.png'
            elif str(self.dicesNumbers[i]) in 'de3':
                dices[i] = './assets/dices/de3.png'
            elif str(self.dicesNumbers[i]) in 'de4':
                dices[i] = './assets/dices/de4.png'
            elif str(self.dicesNumbers[i]) in 'de5':
                dices[i] = './assets/dices/de5.png'
            else:
                dices[i] = './assets/dices/de6.png'
        print(self.dicesUI)

    def getDicesUI(self):
        return self.dicesUI

    def getDices(self):
        return self.dicesNumbers

