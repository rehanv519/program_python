i = 1   #While
while i < 6:
  print(i)
  i += 1
  i = 1  #Break
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  i = 0  #Continue
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  i = 1   #Else 
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")