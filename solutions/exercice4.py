name1=input("enter the name of the first person : ")
age1=int(input("how old are they :  "))
name2=input("enter the name of the second person : ")
age2=int(input("how old are they : "))

if age1>age2 :
    print(f" {name1} is older then {name2}")
elif age2>age1 :
    print(f" {name2} is older then {name1}")
else :
    print(f"they are the same age ! ")
