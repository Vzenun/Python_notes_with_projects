import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator! ")
print("How many words would you like in your password?")
a=int(input("->"))
print("How many symbols would you like in your password?")
b=int(input("->"))
print("How many numbers would you like in your password?")
c=int(input("->"))
d=[letters,symbols,numbers]
s=""
for i in range(a):
    s=s+random.choice(letters)
for i in range(b):
    s=s+random.choice(symbols)
for i in range(c):
    s=s+random.choice(numbers)
print(f'Weak password:{s}')
p=''
for i in range(a+b+c):
    p=p+random.choice(random.choice(d))
print(f'SStrong password:{p}')