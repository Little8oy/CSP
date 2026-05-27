#nico
#Initial Conditions
finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0         #Starting Position
is_hare_asleep = False #Hare starts Awake
x=0
y=0
import random
# The Simulation Loop
for i in range(100000):
    tortoise_pos = 0  #Starting Position
    hare_pos = 0         #Starting Position
    while tortoise_pos < finish_line and hare_pos < finish_line:
        # Tortoise always moves a short distance between 1 - 3 meters at random
        tortoise_pos = tortoise_pos + random.randint(1,3)
        # Hare has a 30% chance of falling a sleep for a turn
        sleep_num = random.randint(1,100)
        if sleep_num<=77:
            #Hair is asleep
            hare_pos = hare_pos
        # If Hare is awake, it will move 1 - 10 meters at random
        else:
            hare_pos = hare_pos + random.randint(1,10)
        # Print the positions of the Hare and Tortoise after each round
    if tortoise_pos >= finish_line:
        x=x+1
    else:
        y=y+1
print(y)
print(x)
