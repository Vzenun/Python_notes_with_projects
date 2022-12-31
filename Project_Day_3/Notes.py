#if/else statement
a=4
if(a==4):
    print("It is 4")
else:
    print("It is not 4")

print("Welcome to the roller coaster ride!")
height=(int(input("Please enter your height in cm: ")))
if(height>=150):
    print("Eligible")
else:
    print("Not eligible")

#Nested if-else statement

n=int(input("Enter the number: "))
if(n%2==0):
    if(n%5==0):
        print("Number is divisible by 10")
    else:
        print("Number is divisible by 2")
else:
    print("Number is not divisible by 2")

#elif statements
if(n%2==0 and n%5==0):
    print("Number is divisible by 10")
elif(n%2==0 and n%5!=0):
    print("Number is divisible by 2 only")
elif(n%2!=0 and n%5!=0):
    print("Number is not divisible by 2 and 5")
else:
    print("Number is divisible by 5 only")

#multiple if statements
if(n%2==0 or n%5==0):
    print("Number is divisible by 2 or 5 or both")
if(n%20==0):
    print("Number is divisible by 20 also")
if(n<0):
    print("Number is less than 0")
if(n>100):
    print("Number is > than 100")
if(not 500):
    print("Number is not 500")
