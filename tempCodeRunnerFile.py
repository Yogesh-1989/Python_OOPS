def addOddNumbers(*args):
  
  sum = 0
  for i in (args):
    sum+=i
  return sum

output = addOddNumbers(10,5,20,3,6)
print("Sum of all these numbers is: ", output)
  