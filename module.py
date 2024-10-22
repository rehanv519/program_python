import platform  #Built-in Modules
x = platform.system()
print(x)
import platform #Using the dir() Function
x = dir(type(platform))
print(x)
import camelcase as cl  #Using a Package
c = cl.CamelCase()
txt = "Hello world"
print(c.hump(txt))
