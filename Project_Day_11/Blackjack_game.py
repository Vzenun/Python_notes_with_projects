from replit import clear
from art import logo
import random

def another_card(list,player_list):
    player_list.append(list[random.randint(0,12)])

def display_pl(player_list,sol):
    print(f'Your cards: {player_list},current score: {sol}')
    
def game(list):
    print(logo)
    player_list=[]
    dealer_list=[]
    another_card(list,player_list)
    another_card(list,player_list)
    another_card(list,dealer_list)
    another_card(list,dealer_list)
    if(player_list[0]==11 and player_list[1]==11):
        player_list[1]==1
    sol=sum(player_list)
    if(dealer_list[0]==11 and dealer_list[1]==11):
        dealer_list[1]==1
    kol=sum(dealer_list)
    if(kol==21):
        display_pl(player_list,sol)
        print(f"Computer's first card: {dealer_list[0]}")
        print(f"Your final hand: {player_list}, final score: {sol}")
        print(f"Computer's final hand: {dealer_list}, final score: 0")
        print("You lose, opponent has blackjack.")
        game_start()
    elif(sol==21):
        display_pl(player_list,sol)
        print(f"Computer's first card: {dealer_list[0]}")
        print(f"Your final hand: {player_list}, final score: 0")
        while(kol<17):
            another_card(list,dealer_list)
            for j in range(len(dealer_list)):
                if(dealer_list[j]==11 and sum(dealer_list)>21):
                    dealer_list[j]=1
            kol=sum(dealer_list)
        print(f"Computer's final hand: {dealer_list}, final score: {kol}")
        if(sol==kol):
            print("It's a draw.")
            game_start()
        else:
            print("You win, with a blackjack.")
            game_start()
    else:
        display_pl(player_list,sol)
        print(f"Computer's first card: {dealer_list[0]}")
        ans=input("Type 'y' to get another card, type 'n' to pass: ")
        while(ans=='y' and sol<=21):
            another_card(list,player_list)
            for j in range(len(player_list)):
                if(player_list[j]==11 and sum(player_list)>21):
                    player_list[j]=1
            sol=sum(player_list)
            display_pl(player_list,sol)
            print(f"Computer's first card: {dealer_list[0]}")
            if(sol<=21):
                ans=input("Type 'y' to get another card, type 'n' to pass: ")
        if(sol==21):
            display_pl(player_list,sol)
            print(f"Computer's first card: {dealer_list[0]}")
            print(f"Your final hand: {player_list}, final score: {sol}")
            while(kol<17):
                another_card(list,dealer_list)
                for j in range(len(dealer_list)):
                    if(dealer_list[j]==11 and sum(dealer_list)>21):
                        dealer_list[j]=1
                kol=sum(dealer_list)
            print(f"Computer's final hand: {dealer_list}, final score: {kol}")
            if(sol==kol):
                print("It's a draw.")
                game_start()
            else:
                print("You win.")
                game_start()
        elif(sol>21):
            print(f"Your final hand: {player_list}, final score: {sol}")
            while(kol<17):
                another_card(list,dealer_list)
                for j in range(len(dealer_list)):
                    if(dealer_list[j]==11 and sum(dealer_list)>21):
                        dealer_list[j]=1
                kol=sum(dealer_list)
            print(f"Computer's final hand: {dealer_list}, final score: {kol}")
            print("You went over and lose the game.")
            game_start()
        else:
            print(f"Your final hand: {player_list}, final score: {sol}")
            while(kol<17):
                another_card(list,dealer_list)
                for j in range(len(dealer_list)):
                    if(dealer_list[j]==11 and sum(dealer_list)>21):
                        dealer_list[j]=1
                kol=sum(dealer_list)
            print(f"Computer's final hand: {dealer_list}, final score: {kol}")
            if(sol==kol):
                print("It's a draw.")
                game_start()
            elif(sol>kol):
                print("You win.")
                game_start()
            elif(kol>sol and kol<21):
                print("You lose.")
                game_start()
            elif(kol>sol and kol==21):
                print("You lose, with a blackjack")
                game_start()
            elif(kol>sol and kol>21):
                print("Opponent went over, you win the game")
                game_start()

def game_start():
    start=input("Do you wanna play the game of Blackjack again? Type 'y' or 'n': ")
    if(start=='y'):
        clear()
        list_game=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        game(list_game)
    else:
        quit()

def game_initial():
    start=input("Do you wanna play the game of Blackjack? Type 'y' or 'n': ")
    if(start=='y'):
        clear()
        list_game=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        game(list_game)
    else:
        quit()
game_initial()