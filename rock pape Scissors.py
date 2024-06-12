import random

l = ["rock", "paper", "scissor"]

while True:
    Ccount = 0
    ucount = 0
    userchoice = int(input('''
Game start...
1 yes
2 No 

      '''))
    if userchoice == 1:
        for a in range(1, 6):
            userinput = int(input('''
1 Rock
2 scissor
3 paper
       ''')) 
            if userinput == 1:
                userchoice = "rock"
            elif userinput == 2:
                userchoice = "scissor"
            elif userinput == 3:
                userchoice = "paper"
                
            Computerchoice = random.choice(l)
            
            if Computerchoice == userchoice:
                print("computre value", Computerchoice)
                print("User value", userchoice)
                print("Game Draw")
                ucount = ucount + 1
                Ccount = Ccount + 1
            elif (userchoice == "rock" and Computerchoice == "scissor") or (userchoice == "paper" and Computerchoice == "rock") or (userchoice == "scissor" and Computerchoice == "paper"):
                print("you win")
                ucount = ucount + 1
            else:
                print("computre value", Computerchoice)
                print("User value", userchoice)
                print("computer Win")
                Ccount = Ccount + 1

        if ucount == Ccount:
            print(" Final Game Draw")
            print("user score",ucount)
            print("computer score",Ccount)
        elif ucount>Ccount:
             print(" final You Win")
             print("user score",ucount)
             print("computer score",Ccount)
        else:
             print("final computer win")
             print("user score",ucount)
             print("computer score",Ccount)
        
         
    else:
        break
