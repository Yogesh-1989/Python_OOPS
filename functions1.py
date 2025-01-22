def person_info(name, age, nationality,profession):
  print("Welcome ", name)
  print("Your age is:", age)
  print("I think you are from: ", nationality)
  print("You have been working as: ", profession)
  
repeat = int(input("Enter number: "))
for i in range(repeat):
  name = input("Enter your name: ")
  age = int(input("Enter your age: "))
  nationality = input("Enter your country name: ")
  profession = input("Enter your profession: ")
  
  person_info(name, age, nationality, profession)