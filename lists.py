thislist = ["apple", "banana", "cherry"]    #creating List
print(thislist)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry","apple", "cherry"]    #Length Of List
print(len(thislist))
list2 = [1, 5, 7, 9, 3]   #List With No
print(list2)
list3 = [True, False, False]   #List With Boolean
print(list3)
list1 = ["abc", 34, True, 40, "bool(true)"]
print(list1)
mylist = ["apple", "banana", "cherry"]   #Type
print(type(mylist))
a=list(("apple", "banana", "cherry"))   #List() Constructor
print(a)
thislist = ["apple", "banana", "cherry"]   #Accessing List
print(thislist[0])   
thislist = ["apple", "banana", "cherry"]    #Negative Indexing
print(thislist[-2])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]   #Range Of Indexes
print(thislist[2:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]   #Range Upto 4 but not include the no 4 list items
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]   #Give Start LI to print 
print(thislist[3:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  #Range Of Negative Index
print(thislist[-4:-1])
thislist = ["apple", "banana", "cherry"]   #To Check If the Given item is present in the list or not
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  thislist = ["apple", "banana", "cherry"]    #To replace the LI & Add New One
thislist[1] = "pineapple"
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]   #To Change the specific range
thislist[2:4] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"] #Insert LI to the specified place
thislist[0:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]     #Insert New Items
thislist.insert(2, "watermelon")
print(thislist) 
thislist = ["apple", "banana", "cherry"]  #Appending
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 
thislist = ["apple", "banana", "cherry"]   #Removing
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"] #Remove Specified Index
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]  #Remove With Pop Keyword
thislist.pop(0)
print(thislist)
thislist = ["apple", "banana", "cherry"]  #Remove With Delete Keyword
del thislist[2]
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist
thislist = ["apple", "banana", "cherry"]  #Clearing List
thislist.clear()
print(thislist)
thislist = ["apple", "banana", "cherry"]   #For Loop
for x in thislist:
    print(x)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
       print(x)  
thislist = ["apple", "banana", "cherry"]  #Length With Range
for i in range(len(thislist)):
  print(thislist[i])
thislist = ["apple", "banana", "cherry"]  #While Loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
thislist = ["apple", "banana", "cherry"] #Looping Using List Comprehension
[print(x) for x in thislist]  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  #List Comprehension
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]   #To Check the alphabet "A";
newlist = [x for x in fruits if "a" in x]
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
newlist = [x for x in range(10)]    #Iterables
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]   #Expression
newlist = [x.upper() for x in fruits]
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]   
newlist = ['hello' for x in fruits]
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]  #Sort List Alphanumerically
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]  #Sort Descending
thislist.sort(reverse = True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"] #Case Insensitive Sort
thislist.sort()
print(thislist)
thislist = ["BaNaNa", "OrAnGe", "KiWi", "ChErRy"]
thislist.sort(key = str.lower)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]   #Reverse Order
thislist.reverse()
print(thislist)
thislist = ["apple", "banana", "cherry"]   #Use the copy() method
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]    #Use the list() method
mylist = list(thislist)
print(mylist)
thislist = ["apple", "banana", "cherry"]    #Use the slice Operator
mylist = thislist[:]
print(mylist)
list1 = ["a", "b", "c"]   #Join Two Lists
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

