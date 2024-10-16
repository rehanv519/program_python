def func():   #Basic Function
  print("Hello") 
func()   
def func(name): #Function With Arguement
    print(name + " android")
func("Oppo")   
func("Vivo")
func("realme")
def my_func(fname, lname):  #No. Of Function
  print(fname,lname)
my_func("Rehan", "Valora")
def my_function(*kids):  #Arbitrary Arguments, *args
  print("The youngest child is " + kids[4])
my_function("Emil", "Tobias","John", "Linus","Harry")
def my_func(child3, child2, child1):  #Keyword Arguments
  print("The youngest child is " + child3)
my_func(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
def my_function(**kid): #Arbitrary Keyword Arguments, **kwargs
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
def my_function(food): #Passing a List as an Argument
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
def my_function(x): #Return Values
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
def my_function(x, /): #Positional-Only Arguments
  print(x) 
my_function(3)
def my_function(x): 
  print(x)
my_function(x = 3)
def my_function(*, x): #Keyword-Only Arguments
  print(x)
my_function(x = 3)
def my_function(x): 
  print(x)
my_function(3)
def my_function(a, b, /, *, c, d): #Combine Positional-Only and Keyword-Only
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)
def recursion(k):  #Recursion
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
recursion(6)
