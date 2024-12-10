day=input("please enter the day of the week : ")
products=int(input("how many items do you have : "))
amount=float(input("what is your totale price : "))

if (day=="saturday" or day=="sunday"):
    if(products >= 5):
      print(f" total price after discount :  {amount - amount*0.25}")
    else:
       print(f" total price after discount :  {amount - amount*0.20}")
else :
    if(products >= 5):
      print(f" total price after discount :  {amount - amount*0.15}")
    else:
       print(f" total price after discount :  {amount - amount*0.10}")
