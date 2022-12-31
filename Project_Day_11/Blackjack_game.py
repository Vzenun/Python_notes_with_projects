from replit import clear
from art import logo
import random
def check(sum_pl,sum_dl):
    if(sum_dl>21):
        print("Hooray!! you win the game.")
    elif(sum_pl>21):
        print("You lose the game.")
    elif(sum_dl>sum_pl):
        print("You lose the game.")
    elif(sum_pl>sum_dl):
        print("You win the game.")
    else:
        print("It is a draw!!")
    game_start()

def another_card(list,player_list):
    player_list.append(list[random.randint(0,12)])

def display_pl(player_list):
    print(f'Your cards: {player_list},current score: {sol}')
    
def game(list):
    print(logo)
    player_list=[]
    another_card(list,player_list)
    another_card(list,player_list)
    if(player_list[0]==11 and player_list[1]==11):
        player_list[1]==1
    sol=sum(player_list)
    if(sol==21):
        print("Hooray!! you win the game.")
    else:
        display_pl(player_list)
        another_card(list,dealer_list)
        print(f"Computer's first card: {dealer_list}")
        ans=input("Type 'y' to get another card, type 'n' to pass: ")
        while(ans=='y' and sol<=21):
            another_card(list,player_list)
            ans=input("Type 'y' to get another card, type 'n' to pass: ")
        if(sol>21):
            print("You lose the game.")
            game()
        else:
            another_card(list,dealer_list)
            if(dealer_list[0]==11 and dealer_list[1]==11):
                dealer_list[1]==1
            sol2=sum(dealer_list)
            if(sol==21):
                print("Hooray!! you win the game.")

def game_start():
    start=input("Do you wanna play the game of Blackjack? Type 'y' or 'n': ")
    if(start=='y'):
        clear()
        dic=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        game(list)
    else:
        quit()
