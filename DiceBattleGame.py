import random
win = 0
lose = 0
draw = 0
print("this is a dice battle game, the one with the higher number wins")
ask = input("do you want to start?:- ")
while ask == "yes":
    computer = random.randint(1,6)
    you = random.randint(1,6)
    ask = input("play next round?- ")
    if ask == "yes" and computer > you:
        print(f"you lose! your no.- {you}, computer no.- {computer}")
        lose = lose + 1
    elif ask == "yes" and computer < you:
        print(f"you win! your no.- {you}, computer no.- {computer}")
        win = win + 1
    elif ask == "yes" and computer == you:
        print(f"draw! your no.- {you}, computer no.- {computer}")
        draw = draw + 1
    elif ask == "no":
        print(f"thanks for playing! win- {win}, lose- {lose}, draw- {draw}")
    else:
        print("invalid credentials")
    
    
     