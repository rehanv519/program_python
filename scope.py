def myfunc():   #Local Scope
  x = 300
  print(x)
myfunc()
def myfunc(): #Function Inside Function
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()
x = 300 #Global Scope
print(x)
def myfunc():
  print(x)
myfunc()
print(x)
x = 300  #Naming Variables
def myfunc(): 
  x = 200
  print(x)
myfunc()
print(x)
def myfunc(): #Global Keyword
  global x
  x = 300 
myfunc()
print(x)
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
def myfunc1(): #Non-Local Keyword
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1())