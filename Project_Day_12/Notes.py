# Now we are going to talk about the scope


# example here 

a=1 
# above a is accesible anywhere as it is in the global scope 

def increement():
    a=5 # this a is valid and accesible only inside the function walls not the outside
    a+=1
    print(f'Inside :{a}')   # 1

increement()
print(f'Outside :{a}')      # 2

# Here this cooncept is called the namespace that is everything which has a name associated with
#  it has a space in which that name is accessible and valid

# Now unlike some other programming languages like c++,java there is no block scope in python
# if we create a variable in a function then it will only be available inside that function

# if we create a variable inside the if block else block or for loop or while loop or 
# anything with the semicolon and indentation then it will not count as the separate local scope at all

# Now question arises how to make changes i.e, modify in the global scope if in function as we have seen
# above it make entirely diff variable inside that function

################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) this will give the name error

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.14159
URL = "https://www.google.com"