#Data Types
#String
print("Hello"[0])#This method of pulling out characters from the string is also known as sub scripting
print("Hello"[-1])
print("123"+"456")

#Integer
print(123+456)
print(123_456)

#Float (floating point number)
print(3.1456)

#boolean
True
False

#len(2345) would give a type error as we cannot give diff data type as an input to len() fn.
num=len(input("What is your name?"))

#formatted strings help to directly print variable value instead of first converting into the string data type
print(f'Your name has {num} characters.')
print(type(num))

#we can also do type casting
num_char=str(len(input("What is your name?")))
print("Your name has "+num_char+" characters.")

#power
print(2**3)
#int() data type converter act as GIF fn.
print(int(8/3))#this int data type converter would actually chop off everything that is after the decimal

#round how to do that
print(round(8/3))#it would actually give 3
print(round(8/3,2))#here if we want to round it upto certain precision we would actually use this.

#floor division
print(8//3)
print(type(8//3))#it is int

#
score=1
score+=9
score*=45