#NFL
#the purpose of my program is to help user on basic info on the nfl teams in 2019-2020 season
#Init
import pandas as pd
data=pd.read_csv('nfl2.csv')
id = data["id"].tolist()
conference = data['Conference'].tolist()
division = data['Division'].tolist()
team = data['Team'].tolist()
city = data['City'].tolist()
capacity = data['Capacity'].tolist()
head_coach = data['Head coach'].tolist()
image = data['Image'].tolist()
stadium = data['Stadium'].tolist()
filter = []


print("Welcome to NFL 2019-2020 Basic info!")
def main():
    while True:
        todo=input("What basic info would you like to find out about the teams in this season the headcoach,the team in said city, conf/div teams, stadium_name. (headcoach,conf/div,stadium,exit) ")

        if todo.lower()=='headcoach':
            coach=input("What teams head coach name do you want to know?: ").title()
            coachhead(coach)
            continue

        if todo.lower()=='conf/div':
            conf=input("What Confrence do youw want to see (AFC,NFC): ").upper()
            div=input("What is the divison in the confrecne you want to see (North,South,East,West?: ").title()
            NFLDiv(conf, div)
            continue
        if todo.lower()=='stadium':
             Stadium_name=input("what NFL team stadium name do you want to know: ").title()
             NFLStadium(Stadium_name)
        if todo.lower()=='exit':
            break


def NFLDiv(conf, div): #this function helps the user see what teams are in said confreence/divison
        for i in range(len(conference and division)):
            if(conf)in conference[i] and (div)in division[i]:
                filter.append(team[i])

        print(filter)

        filter.clear()


def NFLStadium(Stadium_name):
        for i in range(len(stadium)):
            if(Stadium_name)in team[i]:
                filter.append(stadium[i])

        print(filter)

        filter.clear()


def coachhead(coach): #this function shows the head coahc of the nfl team the user wants to see
    for i in range(len(head_coach)):
        if coach in team[i]:
            filter.append(head_coach[i])
    print(filter)

    filter.clear()


main()
