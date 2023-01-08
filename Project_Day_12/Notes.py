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

