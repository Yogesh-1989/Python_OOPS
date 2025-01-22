def bank_balance(balance):
  if balance >=500:
    return True
  else:
    return False
  
  bankers = int(input("Number of bank customers: "))
  for i in range(bankers):
      first_name = input("Enter the first name: ")
      balance = float(input("Enter their bank balance: "))
    
      res = bank_balance(balance)
      print(f"Enough funds in {first_name}s account")
      if res==True:
        print("Dont worry, you have enough funds")
      else:
        print("You dont have enough funds in your account")