#Randomisation and python lists

import random    #random module in the python libraries
import my_module
print(random.randrange(2,6,3))  #it basically returns the random number of form 2=<2+3k<50

print(random.randint(2,8))  #it basically returns the random number k such that 2=<k<=8

print(random.random()) # returns the random float between 0.0(inclusive) and 1.0(excluding)

#Now ques areises how to execute decimal number between 0 and 5(excluding);

print(random.randrange(0,5,1)+random.random());
print(random.random()*5)
print(f'Your love score is {random.randint(0,100)}')

#lists can store any object of any data type
list=[1,'a',4.234,"DWHFSWDBH",32748,32552,245,3,45,43,5,435,]
print(list)
# We can get the value of the list object just by indexing or offset
print(list[3])
print(list[-1])

#lists are actually mutable
list[5]="America" #this is how we can change the value of the already existing list element
list.append(5.45)#append the elment at the end of the list

list.extend([1.44,2,3,4,5,6,7,9]) # add all the input list element to the end of the list "list"

list.insert(0,"dbhhvjhfv")# insert the element at a specific position
list.remove(4)# remove first element of the list which is equal to 4
a=list.remove(0) #remove the element at ith position in the list and return it

list.clear() #remove all elements of the list
del(list[:]) #remove all elements of the list

#and there are many more
print(len(list))# return the number of elements in the list

#Index error lis index out of the range error
#There can be list of the list

