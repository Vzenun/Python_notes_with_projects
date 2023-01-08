import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.")
y=input()
if y=="0":
    print(rock)
if y == "1":
    print(paper)
if y=="2":
    print(scissors)
z=str(random.randint(0,2))
print("Computer chose: ")
if z=="0":
    print(rock)
if z == "1":
    print(paper)
if z=="2":
    print(scissors)
if (z=="0" and y=="0") or (z=="1" and y=="1") or(z=="2" and y=="2"):
    print("It's a draw.")
if (z=="0" and y=="1") or (z=="1" and y=="2") or(z=="2" and y=="0"):
    print("You won!")
if (z=="0" and y=="2") or (z=="1" and y=="0") or(z=="2" and y=="1"):
    print("You lose")