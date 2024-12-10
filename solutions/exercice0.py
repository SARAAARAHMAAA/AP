people=int(input("how many people need a ride? : "))
peoplepertaxi=int(input("how many people can fit into a texi ? : "))

nb=people//peoplepertaxi
reste= people%peoplepertaxi
print(nb)
print(reste)

if reste==0 :
    print(f" you will need : {nb}")
else :
    print(f"you will need : {nb +1}")
    


