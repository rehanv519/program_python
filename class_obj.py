class MyClass:   #Create Class & Obj 
  x = 5
p1 = MyClass()
print(MyClass)
print(p1.x)     
class Person: #The __init__() Function
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
class Person: 
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1)
print(Person)
class Person:  #The __str__() Function
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"    
p1 = Person("John", 36)
print(p1)
class Person:   #Object Methods
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
    print("And I'm ",self.age," years old")
p1 = Person("Sahil", 19)
p1.myfunc()
class Person:  #The Self Parameter
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
    print("And I'm  ",abc.age," years old")
p1 = Person("John", 36)
p1.myfunc()
class Person:  #Modify Object Properties
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is ",self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)
class Person:  #Delete Object And Properties
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
del p1





