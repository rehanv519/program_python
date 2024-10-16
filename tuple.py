a = ("apple", "banana", "cherry","pineapple")    #Tuple 
print(a)
b = ("apple", "banana", "cherry", "apple", "cherry")
print(b)
c = (("apple", "banana", "cherry","pineapple","strawberry","mango"))  #Tuple Length
print(len(c))
d = ("apple","mango","strawberry") #Get Type
print(type(d))
e = ("apple", "banana", "cherry","mango","guava")
print(e)
f = (1, 5, 7, 9, 3, 4, 8)   #Numbers As Tuple
print(f)
g = (True, False, False,True,False)  #Booleans As Tuples
print(g)
h = tuple(("apple", "banana", "cherry")) #Constuctor
print(h)
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry")  #Negative Indexing
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")  #Range Of Index
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") #Range Of Negative Index
print(thistuple[-4:-1])
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
x = ("apple", "banana", "cherry")  #Change Tuple Values
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
thistuple = ("apple", "banana", "cherry") #Add Items
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
thistuple = ("apple", "banana", "cherry") #Add Tuple With Tuple
y = ("orange",)
thistuple += y
print(thistuple)
thistuple = ("apple", "banana", "cherry") #Remove Items
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
thistuple = ("apple", "banana", "cherry") #Delete with del Keyword
del thistuple
fruits = ("apple", "banana", "cherry") #Unpacking Tuple
print(fruits)
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry") #Use *
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
thistuple = ("apple", "banana", "cherry") # For Loop
for x in thistuple:
  print(x)
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)): #Looping with Index
  print(thistuple[i])  
thistuple = ("apple", "banana", "cherry") #While Loop
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
tuple1 = ("a", "b" , "c") #Join Tuples
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry") #Multiply Tuples
mytuple = fruits * 2
print(mytuple)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5) #Count
x = thistuple.count(5)
print(x)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5) #Search First Occurrence
x = thistuple.index(8)
print(x)