def grade(score):
  print("Your score is:", score)
  if score >0 and score <=50:
    print("Below passing, Improve your grade.!")
    
  elif score >50 and score <=70:
    print("Barely passing the class.!")
    
  elif score >70 and score <=90:
    print("You are under few brillinat minds of class.!")
  else:
    print("You are topper of the class.!")
    
score = int(input("Enter your score: "))

grade(score)