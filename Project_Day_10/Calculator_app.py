from art import logo

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2


def calculator(sign,num1):
    op=input("Pick an operation: ")
    if(op not in sign):
        print(f"Invalid operation {op} Type again! ")
        calculator(sign,num1)
    else:
        num2=float(input("What is the next number? "))
        sol=0
        if(op=='+'):
            print(f'{num1} {op} {num2} = {add(num1,num2)}')
            sol=add(num1,num2)
        elif(op=='-'):
            print(f'{num1} {op} {num2} = {sub(num1,num2)}')
            sol= sub(num1,num2)
        elif(op=='*'):
            print(f'{num1} {op} {num2} = {mul(num1,num2)}')
            sol= mul(num1,num2)
        elif(op=='/'):
            print(f'{num1} {op} {num2} = {div(num1,num2)}')
            sol=div(num1,num2)
        next_step=input(f'Type "y" to continue calculating with {sol} or type "n" to start a new calculation or type "ex" to stop calculating and exit the application: ')
        if(next_step=='y'):
            calculator(sign,sol)#This is an example of the recursion.
        elif(next_step=='n'):
            restart()
        elif(next_step=='ex'):
            print("Thank u for using the calculator.")
            quit()
        
def restart():
    print(logo)
    num1=float(input("What is the first number? "))
    sign=['+','_','*','/']
    for i in sign:
        print(i)
    calculator(sign,num1)
restart()

