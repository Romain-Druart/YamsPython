import random

dicesNumbers = [0, 0, 0, 0, 0]
check = 1

for i in range(len(dicesNumbers)):
  if check == 0:
    dicesNumbers[0] = random.randint(1, 6)
          # change dice value
  dicesNumbers[1] = random.randint(1, 6)
            # cahnge dice value
  dicesNumbers[2] = random.randint(1, 6)
  if check == 0:
    # cahnge dice value
    dicesNumbers[3] = random.randint(1, 6)
        # cahnge dice value
  dicesNumbers[4] = random.randint(1, 6)
            # cahnge dice value
        # dices[i]= random.randint(1, 6)
print(dicesNumbers)