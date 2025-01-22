

def add(x,y):
  
  print("x:", x)
  print("y:", y)
  sum = x+y
  return sum

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("The sum is", add(a,b))
print(f"Therefore sum of {a} and {b} is {a+b}")