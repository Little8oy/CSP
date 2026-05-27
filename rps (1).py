#nico
#intialzie
import random
#functions
def rps():
    wins=0
    losses=0
    ties=0
    while True:
        x= random.randint(1,3)
        #1 is rock
        #2 is paper
        #3 is rock
        choice= input("what do you chose Rock Paper or Scissors or quit: ")
        if choice==("quit"):
            break
        if choice=="rock" and x==1:
            print ("you tied")
            ties=ties+1

        if choice=="rock" and x==2:
            print ("you lost")
            losses=losses+1

        if choice=="rock" and x==3:
            print ("you won")
            wins=wins+1

        if choice=="paper" and x==1:
            print ("you won")
            wins=wins+1

        if choice=="paper" and x==2:
            print ("you tied")
            ties=ties+1

        if choice=="paper" and x==3:
            print ("you lost")
            losses=losses+1

        if choice=="scissors" and x==1:
            print ("you lost")
            losses=losses+1

        if choice=="scissors" and x==2:
            print ("you won")
            wins=wins+1
            
        if choice=="scissors" and x==3:
            print ("you tied")
            ties=ties+1
            continue
        print("wins:",wins)
        print("losses:",losses)
        print("ties:",ties)
#main
print("welcom to rock papper scissors you will be playing the computer now lets play")
rps()
