try:
    import random
except ImportError :  
  print("exception in importing module")


class Dice(object):


    def __init__(self, *args, **kwargs):
        self.dicesNumbers = [0,0,0,0,0]
        self.dicesUI = [0,0,0,0,0]
        self.shuffleDices(self.dicesUI)
        print(self.dicesNumbers)

    def shuffleDices(self, dices):
        for i in range(len(self.dicesNumbers)):
            dices[i]= random.randint(1, 6)
        self.dicesNumbers = dices
        self.displayDices(self.dicesNumbers)
        self.getDicesUI()           
        return self.dicesNumbers

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

