from replit import clear
import art
# we can call this function clear from the replit module wheneve we want to clear the console.abs
print(art.logo)
print("Welcome to the secret auction programme")
finish=True
max=0
dict_participants={}
while(finish):
    name=input("Input your name: ")
    bid=int(input("Enter your bid value: "))
    k=(input("Are there any other bidders? ('Yes' or 'No')"))
    if(k=='No'):
        finish=False
    dict_participants[name]=bid
    clear()
max=0
name=''
for i in dict_participants:
    if(dict_participants[i]>max):
        max=dict_participants[i]
        name=i
print(f'The winner is {name} with a bid of {max}$')