import random

dicesNumbers = [0,0,0,0,0]
dicesUI = []


def shuffleDices(dices):
    # print("Passage dans fonction shuffleDices \n")
    for i in range(len(dices)):
        print("\n Shuffle")
        dices[i]=random.randint(1, 6)
        print(dices[i])


def displayDices(dices):
    # print("Passage dans fonction displayDices \n")
    for i in range(len(dicesNumbers)):
        # print("dans le for de display ")
        print(dices[i])
        if str(dicesNumbers[i]) in 'de1':
            dices.append('de1.png')
            print('de1.png \n')
        elif str(dicesNumbers[i]) in 'de2':
            dices.append('de2.png')
            print('de2.png \n')
        elif str(dicesNumbers[i]) in 'de3':
            dices.append('de3.png')
            print('de3.png \n')
        elif str(dicesNumbers[i]) in 'de4':
            dices.append('de4.png')
            print('de4.png \n')
        elif str(dicesNumbers[i]) in 'de5':
            dices.append('de5.png')
            print('de5.png \n')
        else:
            dices.append('de6.png')
            print('de6.png \n')


shuffleDices(dicesNumbers)

displayDices(dicesUI)
print('\n dicesNumbers')
print(dicesNumbers)
print('\n dicesUI')
print(dicesUI)


#######################################
# def my_function(food):
#  for i in dices:
#  	print(i)

# dices = []

# for i in range(1,6):
#  	dices.append(random.randint(1,6))

# my_function(dices)
