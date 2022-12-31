#This is how we comment in python

#print command in the python and it automatically goes to next line
print("Hello World")
print("a\nB\nC")

print("Hello"+"Angela")#This is what we call as String concatenation.
print('Concatenation is done with the help of "+" sign.')

#variables
name_your="Vidur"

#formatted string use
print(f'How are you {name_your}')
name=input("What is your name?")#this is how we are going to take as an input
print(f'Hello {name}')

print("Hello "+input("What is your name?"))#In python by default input is taken as a string

#how to determine length of a string for that we are going to use the len() function
print(len(name))

#in python we can switch the variables like this
s=10
b=5
s,b=b,s
print(f'{b} {s}')