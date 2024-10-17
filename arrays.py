cars = ["Ford", "Volvo", "BMW"]   #Basic Array
print(cars)
cars = ["Ford", "Volvo", "BMW"]   #Get Type
print(type(cars))
cars = ["Ford", "Volvo", "BMW"]  #Access Elements
x = cars[0]
print(x)
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
cars = ["Ford", "Volvo", "BMW"]  #Length Of Array
x = len(cars)
print(x)
cars = ["Ford", "Volvo", "BMW"]  #Looping
for x in cars:
  print(x)
cars = ["Ford", "Volvo", "BMW"] #Adding Array Elements
cars.append("Honda")
print(cars)  
cars = ["Ford", "Volvo", "BMW"]  #Removing Array Elements
cars.pop(1)
print(cars)
cars = ["Ford", "Volvo", "BMW"]   #Removing  By Remove Keword
cars.remove("Volvo")
print(cars)
fruits = ["apple", "banana", "cherry"]  #Clearing Array
fruits.clear()
print(fruits)
fruits = ["apple", "banana", "cherry"]  #Copying Items
x = fruits.copy()
print(x)
fruits = ["apple", "banana", "cherry"]  #Count Elements
x = fruits.count("cherry")
print(x)
fruits = ['apple', 'banana', 'cherry']  #Extending Array Elements
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
fruits = ['apple', 'banana', 'cherry'] #Print Index Of The specific Element
x = fruits.index("cherry")
print(x)
fruits = ['apple', 'banana', 'cherry'] #Insert At Specific 
fruits.insert(1, "orange") 
print(fruits)
fruits = ['apple', 'banana', 'cherry']  #Reversing Array
fruits.reverse()
print(fruits)
cars = ['Ford', 'BMW', 'Volvo']  #Sorting Array
cars.sort()
print(cars)



