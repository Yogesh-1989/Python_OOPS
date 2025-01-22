def addNumbers(*args):
  sum = 0
  for i in (args):
    sum = sum + i
  return sum

addition = addNumbers(2,5,8,9,6,3,4,7,8)
print("Sum is: ", addition)