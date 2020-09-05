#Day 2 Assignment MANIKANDAN.N

#1. List and its functions
lst=['manik',"learning python", 3.141, 10]
print('List: ',lst)

print("Length of List: ",len(lst)) # 1. length of list
print("max(lst): ",max(lst)) # 2. print largest value element in the list
print("min(lst): ",min(lst)) # 3. print smallest value element in the list

str="Hello World"
lst1 = list(str) # 4. converting string as list
print(type(lst1), "Str converted: ",lst1)

lst.insert(1, " is ") #5. Inserting in list at given index
print("New list after inserted: ",lst)

lst.reverse()
print("Reversed list: ",lst1)

lst.extend(lst1)
print("Extended list (lst1 added in lst): ",lst)
print("------------------------------------------------------------")
#------------------------------------------------------------

#2. Dictionary and its default functions
a={'name': 'manik', 'date': '2.7.95', 'age': '25', 'status': 'single'}

print("a values: ", a.values())    #1. print only values in dict
dit=a.copy()                     #2. Copy dict fn
print("New dict dit: ",dit)
dit.update({'Degree': "B.E", 'name':"MANIK"})      #3. updating dict
print("New dit: ", dit)
keys=("key 1", "key 2", "key 3")
values=(0)
a=dict.fromkeys(keys,values)
print(type(a), a) #4. creating dict from variables
a.clear()         #5. Clear the dict  
print("d: ",a)
print("------------------------------------------------------------")
#------------------------------------------------------------

#3. sets and its default functions
s1= {10,12,13,14,15,(5,5)}
s2= {1,2,3,4,10,13,15}

name= "manik"
print( "\nname type: ", type(name)) 
name= set(name)     # 1.creating set from str
print(type(name))
sunion=s1|s2
print("sunion: ",sunion)       # 2. union of s1 and s2
sintersect=s1&s2
print("Intersection of sets: ", sintersect) # 3. intersection of s1 & s2
s1diff=s1-s2
print("Diff. s1 from s2", s1diff) #4. diff of s1 from s2
s2diff=s2-s1
print("Diff. s2 from s1", s2diff) #4. diff of s2 from s1
print("Is s2 disjoint of s1? : ", s2.isdisjoint(s1))          #5. check disjoint  
print("------------------------------------------------------------")
#------------------------------------------------------------

#4. Tuple and its methods

tup1 = ("roses","are","red","and","Clouds","are","white" )

print(tup1.count("are")) #1. count of "are" in tup1
print(tup1.index("red")) #2. index of element red in tup1

tup2= (1,2,3,4,5)
tup = tup1 + tup2          #3. Joining tuples (we can't add element in tup) 
print("Final tup: ",tup)
del tup2                    #4. delete tup2 completely
thistup = ("manik",)           #5. single element tuple
print("type of thistup: ",type(thistup))
print("------------------------------------------------------------")
#------------------------------------------------------------

#5. String and its methods

str1 = "manik"
str0  = 'N '
str2 = "physics maths chemistry biology"

print(str1.capitalize()) # 1. Capitalization
print(str2.find('math') ) # 2. finding substring, op. is index
print(str1.join(str0))    # 3. str1 joins with s2 every char
print(str2.split())       # 4. splits at space in str2
print(str2.index('bio',10))       # 5. index of str2 FROM 10th position

