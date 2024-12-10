name1=input("enter the name of the first runner : ")
speed1=float(input("time (in seconds)  :  "))
name2=input("enter the name of the second runner : ")
speed2=float(input("time (in seconds) : "))

if speed1>speed2 :
    print(f"The faster runner is : {name2}")
elif speed2>speed1 :
    print(f"The faster runner is :{name1}")
else :
    print(f"{name1} and {name2} have the same time ! ")
