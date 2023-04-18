import Data

water=Data.resources["water"]
milk=Data.resources["milk"]
coffee=Data.resources["coffee"]
money=0

def resource_checking(code):
    if(code==0):

        a=Data.menu["espresso"]["ingredients"]["water"]
        b=Data.menu["espresso"]["ingredients"]["coffee"]

        if(a>water):
            print(f'Sorry there is not enough water.')
            return False
        
        elif(b>coffee):
            print(f'Sorry there is not enough coffee.')
            return False
        
        else:
            return True

    elif(code==1):
        a=Data.menu["latte"]["ingredients"]["water"]
        b=Data.menu["latte"]["ingredients"]["coffee"]
        c=Data.menu["latte"]["ingredients"]["milk"]

        if(a>water):
            print(f'Sorry there is not enough water.')
            return False
        if(b>coffee):
            print(f'Sorry there is not enough coffee.')
            return False
        if(c>milk):
            print(f'Sorry there is not enough milk.')
            return False
            
        else:
            return True

    elif(code==2):
        a=Data.menu["cappuccino"]["ingredients"]["water"]
        b=Data.menu["cappuccino"]["ingredients"]["coffee"]
        c=Data.menu["cappuccino"]["ingredients"]["milk"]
        if(a>water):
            print(f'Sorry there is not enough water.')
            return False
        if(b>coffee):
            print(f'Sorry there is not enough coffee.')
            return False
        if(c>milk):
            print(f'Sorry there is not enough milk.')
            return False
        
        else:
            return True

def process_coins(code):
    print(f'Please insert coins.')

    a=int(input("how many quarters: "))
    b=int(input("how many dimes: "))
    c=int(input("how many nickles: "))
    d=int(input("how many pennies: "))

    if(code==0):
        cost=Data.menu["espresso"]["cost"]
    elif(code==1):
        cost=Data.menu["latte"]["cost"]
    elif(code==2):
        cost=Data.menu["cappuccino"]["cost"]

    answer=a*0.25+b*0.10+c*0.05+d*0.01

    if(answer>=cost):
        global money
        # global water
        # global coffee
        # global milk
        money+=cost
        print(f'Here is ${round(answer-cost,2)} in change.')
        if(code==0):
            water-=Data.menu["espresso"]["ingredients"]["water"]
            coffee-=Data.menu["espresso"]["ingredients"]["coffee"]
            print(f'Here is your espresso ☕️. Enjoy!')
        elif(code==1):
            water-=Data.menu["latte"]["ingredients"]["water"]
            coffee-=Data.menu["latte"]["ingredients"]["coffee"]
            milk-=Data.menu["latte"]["ingredients"]["milk"]
            print(f'Here is your latte ☕️. Enjoy!')
        elif(code==2):
            water-=Data.menu["cappuccino"]["ingredients"]["water"]
            coffee-=Data.menu["cappuccino"]["ingredients"]["coffee"]
            milk-=Data.menu["cappuccino"]["ingredients"]["milk"]
            print(f'Here is your cappuccino ☕️. Enjoy!')

    else:
        print(f'Sorry that is not enough money. Money refunded.')

def report_printing():
    print(f'Water: {water} ml')
    print(f'Milk: {milk} ml')
    print(f'Coffee: {coffee} g')
    print(f'Money: ${round(money,2)}')
    return

def start():
    answer=input("What would you like? (espresso/latte/cappuccino): ")
    if(answer=="espresso"):
        if(resource_checking(0)):
            process_coins(0)
            start()
        else:
            start()
    elif(answer=="latte"):
        if(resource_checking(1)):
            process_coins(1)
            start()
        else:
            start()
        
    elif(answer=="cappuccino"):
        if(resource_checking(2)):
            process_coins(2)
            start()
        else:
            start()
        
    elif(answer=="report"):
        report_printing()
        start()
    
    elif(answer=="off"):
        return

start()
