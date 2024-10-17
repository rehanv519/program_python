x = lambda a,b: a + b #Addition
print(x(50,70))
x = lambda a, b: a * b  #Multiplication
print(x(15, 60))
x = lambda a, b, c: a + b + c  
print(x(5, 6, 2))
def func(n):   #Lambda Function
    return lambda a : a * n
c = func(2)
d = func(8)
print(c(11))
print(d(99))


