import random
rows=int(input("How many quick picks?"))
randomNum=[]

for i in range(rows):
    print("")
    randomNum = []
    for x in range(6):
        num= random.randrange(1,46)
        if num not in randomNum:
            randomNum.append(num)
        else:
            x-=1
        randomNum.sort()
    for j in randomNum:
        print("{:3}".format(j),end="")