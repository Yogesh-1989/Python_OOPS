def person_info(name, age, nationality):
  print("Welcome", name)
  print(f"You are {age} years old")
  print(f"Your nationality is {nationality}")
  
  
member_total = int(input("members:"))
for i in range(member_total):
  name = input("Enter name:")
  age= input("Enter age:")
  nationality= input("Enter nationality:")
  
  
  person_info(name, age, nationality)