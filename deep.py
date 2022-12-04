answer = str(input("what is the meaning of life? "))
true1 = "forty-two"
true2 = "forty two"
if answer == "42":
   print("yes")
elif answer.lower() == true1:
   print("yes")
elif answer.lower() == true2:
   print("yes")
else:
   print("no")
