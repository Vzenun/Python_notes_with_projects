from turtle import Turtle,Screen
from prettytable import PrettyTable

# timmy=Turtle()
#  this is how we construct our new object
# print(timmy)
# timmy.shape("turtle")
# <turtle.Turtle object at 0x104b73940>
# myscreen=Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()

table = PrettyTable()
print(table)
table.add_column("Pokemon",["Pickachu","Turtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table.align)
table.align='l'
print(table)