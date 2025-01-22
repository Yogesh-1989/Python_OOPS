def mortgage(cash):
  if cash >=50000:
    print("Instant approval.!")
    
  elif cash < 50000 and cash >=20000:
    print("You need an approval.!")
    
  else:
    print("Not approved for mortgage.!")
    
cash = int(input("How much cash do you have.?: "))
total_balance = 0
while cash != 0:
  total_balance+=cash
  mortgage(cash)
  cash = int(input("How much cash do you have.?: "))
  
  
print("Total money requested:", total_balance)
    