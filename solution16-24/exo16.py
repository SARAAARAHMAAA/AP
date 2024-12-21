possibility = True
while possibility: 
    tab=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    choice=int(input("enter an index please (-1 to quit) : "))

    if choice>0 and choice < len(tab) :
        new=input("please enter the new value")
        tab[choice]=new

        for index, element in enumerate(tab):
          print(f"Index {index} : {element}")

    elif choice > len(tab):
       print(f"this index doesnt exist please choose between 0 and {len(tab)-1}")
    elif choice ==-1 :
       possibility= False 
    else : 
       print("please enter a valid index !")
    
print("thank you have a good day ! ")