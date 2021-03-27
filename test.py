import random

dicesNumbers = [0,0,0,0,0]
numberOfToss = 0

isOneChecked = 0
isTwoChecked = 0
isThreeChecked = 0
isFourChecked = 0
isFiveChecked = 0


def dices ():
  if isOneChecked == 0:
    print('Dice 1')
    dicesNumbers[0] = random.randint(1, 6)
  if isTwoChecked == 0:
    print('Dice 2')
    dicesNumbers[1] = random.randint(1, 6)
  if isThreeChecked == 0:
    print('Dice 3')
    dicesNumbers[2] = random.randint(1, 6)
  if isFourChecked == 0:
    print('Dice 4')
    dicesNumbers[3] = random.randint(1, 6)
  if isFiveChecked == 0:
    print('Dice 5')
    dicesNumbers[4] = random.randint(1, 6)
  print(dicesNumbers)
  for i in range(len(dicesNumbers)):
    dicesNumbers[i] = random.randint(1, 6)
  return dicesNumbers

print(dices())