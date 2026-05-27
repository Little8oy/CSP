#Nico
#functions
def movie():
    age= input("please enter your age: ")

    if int (age) >= 18:
        print ("you can watch any movie including rated R")

    elif int (age) >=13:
        print("you can watch any movie up to PG 13")
    else:
        print("you can only watch pg movies")

#main
movie()
