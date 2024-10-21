mytuple = ("apple", "banana", "cherry") #Tuple Iterator
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
mystr = "banana" #String Iterator
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
mytuple = ("apple", "banana", "cherry") #Looping in Iterator
for x in mytuple:
  print(x)
mystr = "banana"
for x in mystr:
  print(x)
class MyNumbers: #Create an Iterator
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
class MyNumbers:  #Stop Iteration
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 50:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)
  