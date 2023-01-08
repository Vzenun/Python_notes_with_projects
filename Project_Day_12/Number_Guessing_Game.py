from art import logo
from replit import clear
from random import randint

number=0

EASY_LEVEL_TURNS=10
MEDIUM_LEVEL_TURNS=7
DIFFICULT_LEVEL_TURNS=5

def win_game():
    print(f'You got it,the answer was {number}')
    game_again()

def lose_game():
    print(f'You have run out of guesses, you lose the game')
    game_again()

def game_again():
    query=input(f'Type "y" if you want to play again else type "n" to quit: ')
    if(query=='y'):
        game_initiate();
    else:
        exit()

def level(query):
    if(query==0):
        turn_left=EASY_LEVEL_TURNS
    elif(query==1):
        turn_left=MEDIUM_LEVEL_TURNS
    elif(query==2):
        turn_left=DIFFICULT_LEVEL_TURNS
    is_guessed=False
    global number
    while(turn_left!=0 and not is_guessed):
        print(f'You have {turn_left} attempts remaining to guess the number.')
        num=int(input(f'Guess the number: '))
        if(num>number):
            print("Too high!")
        elif(num<number):
            print("Too low!")
        else:
            is_guessed=True
            win_game()
        turn_left-=1
    lose_game()

def game_initiate():
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    global number
    number=randint(1,100)
    print(f'Pssst, the correct answer is {number}')
    query=int(input(f'Choose a difficulty. Type "0" for easy or "1" for medium or "2" for hard: '))
    level(query)

game_initiate()