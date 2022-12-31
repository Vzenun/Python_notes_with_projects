from Hangman_words import word_list
from Hangmanart import logo
import random
from Hangmanart import stages
print(logo)
chosen_word = random.choice(word_list)
lives=6
y=list(chosen_word)
display=[]
for i in chosen_word:
    display.append("_")
while y!=display and lives>0:
    guess = input("Guess the letter: ")
    guess.lower()
    if guess in (y):
        for i in range(len(y)):
            if y[i] == guess:
                display[i] = guess
        print(stages[lives])
        print(*display, sep=" ")
    else:
        lives-=1
        print(stages[lives])
        print(*display, sep=" ")
if y!=display:
    print("You died!!")
if y==display:
    print("Yay yoy won the game!!")
