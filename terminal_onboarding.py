def terminal_1():
  print("Departing from terminal -1, Budget flight: ")
  flight_check()
  
def terminal_2():
  print("Departing from termianl -2, Domestic flight: ")
  flight_check()
  
def terminal_3():
  print("Departing from terminal -3, International flight: ")
  flight_check()
    
def flight_check():
  answer= input("budget/domestic/international:?").lower()
  if answer=="budget":
    terminal_1()
  if answer=="domestic":
    terminal_2() 
  if answer=="international":
    terminal_3()
  else:
    print("There is no other terminal:")

flight_check()
    
  