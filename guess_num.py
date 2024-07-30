import random
rang = int(input("choose the range between 1-10:"))
won=0
los=0
while True:
    chose= int(input("chose number or press 70 to quit: "))
    ran = random.randint(0,rang)
    if  rang>10:
        print("invalid")
        break

    elif chose== 70:
        print(won,los)
        break
    else:
        if chose==ran:
            print('you won!')
            won+=1

        else:
            los+=1
            print("you lost!")
            