import random
w=0
l=0


# print(comp)

while True:
    ran = random.randint(0,2)
    choice=["rock","paper","scissor"]
    comp = choice[ran]
    # print(comp)
    
    guess= input("enter choice : r , p, s  OR press Q exit : ").lower()

    if guess=="q":
        break

    if comp=="rock" and guess=="p":
        print("won")
        w=w+1
    elif comp=="paper" and guess=="s":
        print("won")
        w=w+1
    elif comp=="scissor" and guess=="r":
        print("won")
        w=w+1
    else:
        print("you loss")
        l=l+1

print(w,l)