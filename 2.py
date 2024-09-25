x = 'python'#print
print(x)
a = 'python'
b = ' is a'
c = ' server side scripting language'
print(a+b+c)
r = 'Website'
s = 'Application'
print(r,s)
print(r+s)
t = 5
u = 'Sahil'
print(t,u)
x = 'interesting'#udf->local
def myfunc():
  print("Python is " + x)
myfunc()
r= 'python'
def func():
    print('Django is a framework of'  ,r)
func()
a=50
def sum():a=30
b=80
print("A + B = ",a+b)
sum()
a=5
print("A + B = ",a+b)
sum()    
a=60
print("A + B = ",a+b)
a=100
b=50
print(a-b)
def sub():global a #udf->global
a=200
b=30
sub()
print(a-b)
sub()
a=150
print(a-b)
print("Hello \nWorld")
a=4   #int
print(a)
print(type(a))           #get the type
b="Hello World"   #str       #datatype
print(b)
print(type(b))
c=30.6     #float
print(c)
print(type(c))
d=3j      #complex
print(d)
print(type(d))
x = ["apple", "banana", "cherry"]   #list
print(x)
print(type(x))
x = ("apple", "banana", "cherry")    #tuple
print(x)
print(type(x))
x=range(80)   #range
print(x)
print(type(x))
x = {"name" : "John", "age" : 36}   #dict
print(x)
print(type(x))
x = {"apple", "banana", "cherry"} #set
print(x)
print(type(x))
x = frozenset({"apple", "banana", "cherry"})   #frozenset
print(x)
print(type(x))
x = True        #bool
print(x)
print(type(x))
x = b"Hello"     #bytes
print(x)
print(type(x))
x = bytearray(5)    #bytearray
print(x)
print(type(x))
x = memoryview(bytes(5))      #memory view
print(x)
print(type(x))
x = None     #nonetype
print(x)
print(type(x))
r = int(1.8)    #typeconversion
print(r)
r=float(1)
print(r)
r=complex(9)
print(r)
import random
print(random.randrange(7))
y=str(2)
print(y)
a='Hello'   #Assign string to Variable
print(a)
a = """Lorem ipsum dolor sit amet,      
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.  """
print(a)

              
