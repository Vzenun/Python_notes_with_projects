import art
import Data
import random
import replit

def main_function(current_score, name ,follower_count, description, country):
    replit.clear()
    print(art.logo)
    print(f'Yes, you are right! Current score: {current_score}')
    print(f'Compare A: {name} , a {description}, from {country}.')
    print(art.vs)
    k=random.choice(Data.data)
    while(k["name"]==name):
        k=random.choice(Data.data)
    # print(k)
    print(f'Against B: {k["name"]} , a {k["description"]}, from {k["country"]}.')
    answer=input("Who has more followers? Type 'A' or 'B':")
    if(answer=="A"):
        if(follower_count>k["follower_count"]):
            current_score+=1
            main_function(current_score, name ,follower_count, description, country)
        else:
            replit.clear()
            print(art.logo)
            print(f'Sorry, that is wrong answer. Final score: {current_score}')
            return
    else:
        if(follower_count<k["follower_count"]):
            current_score+=1
            main_function(current_score, k["name"] ,k["follower_count"], k["description"], k["country"])
        else:
            replit.clear()
            print(art.logo)
            print(f'Sorry, that is wrong answer. Final score: {current_score}')
            return


def start():
    replit.clear()
    print(art.logo)
    current_score=0
    t=random.choice(Data.data)
    print(f'Compare A: {t["name"]} , a {t["description"]}, from {t["country"]}.')
    print(art.vs)
    k=random.choice(Data.data)
    while(k["name"]==t["name"]):
        k=random.choice(Data.data)
    # print(k)
    print(f'Against B: {k["name"]} , a {k["description"]}, from {k["country"]}.')
    answer=input("Who has more followers? Type 'A' or 'B':")
    if(answer=="A"):
        if(t["follower_count"]>k["follower_count"]):
            current_score+=1
            main_function(current_score, t["name"] ,t["follower_count"], t["description"], t["country"])
        else:
            replit.clear()
            print(art.logo)
            print(f'Sorry, that is wrong answer. Final score: {current_score}')
            return
    else:
        if(t["follower_count"]<k["follower_count"]):
            current_score+=1
            main_function(current_score, k["name"] ,k["follower_count"], k["description"], k["country"])
        else:
            replit.clear()
            print(art.logo)
            print(f'Sorry, that is wrong answer. Final score: {current_score}')
            return

start()
