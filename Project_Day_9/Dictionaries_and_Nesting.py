#Dictionaries allow us to group together and tag related pieces


#This is also an example of nested dictionary
encyclopedia={"Animals":["Cow","Hen","Bear","Donkey"],"Plants":["Sunflower","Lotus","Rose"],"Planets":["Mercury","Venus","Mars","Jupiter"]}

#Looping through the dictionary
for i in encyclopedia:
    print(i)
    for j in encyclopedia[i]:
        print(j)

empty_list=[]
empty_dict={}
empty_dict[1]="abcd"
print(empty_dict)

#How to change the existing values of keys of the dictionary
empty_dict[1]="efgh"
print(empty_dict)

#how to wipe out existing non-empty dictionary
empty_dict={}
print(empty_dict)

