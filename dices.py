import random


class Dice():
    dicesNumbers = []
    dicesUI = []

    def __init__(self, *args, **kwargs):

        self.shuffleDices(self.dicesUI)
        self.displayDices(self.dicesNumbers)

    def shuffleDices(self, dices):
        for i in dices:
            dices[i].append(random.randint(1, 6))

    def displayDices(self, dices):
        for i in dices:
            if dices[i] in 'de1':
                self.dicesUI.append('./assets/dices/de1.png')
                print('de1.png')
            elif dices[i] in 'de2':
                self.dicesUI.append('./assets/dices/de2.png')
                print('de2.png')
            elif dices[i] in 'de3':
                self.dicesUI.append('./assets/dices/de3.png')
                print('de3.png')
            elif dices[i] in 'de4':
                self.dicesUI.append('./assets/dices/de4.png')
                print('de4.png')
            elif dices[i] in 'de5':
                self.dicesUI.append('./assets/dices/de5.png')
                print('de5.png')
            else:
                self.dicesUI.append('./assets/dices/de6.png')
                print('de6.png')

# import random


# def my_function(food):
#  for i in dices:
#  	print(i)

# dices = []

# for i in range(1,6):
#  	dices.append(random.randint(1,6))

# my_function(dices)
