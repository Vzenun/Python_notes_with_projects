# Function is identified by the name followed by the paranthesis
#eg:
print("lll")
print(len("Hello"))

#how to define a function with input
#Here a and b are called parameters
def fn_name(a,b):
    print(a+" "+b)

# now we are calling a function.
fn_name("Vidur","Goel")
#we have passed arguments as the positional arguments
fn_name(b="Goel",a="Anjali")
#we have passed arguments as the keyword arguments

#Here "Vidur" and "Goel" are the arguments passed while calling the function

# while loop
a=5
while(a!=0):#while the condition in the paranthesis is true it will keep on iterating
    print(a)
    a-=1
