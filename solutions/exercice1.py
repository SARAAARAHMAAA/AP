name=input("please enter your name :")

if name=="VIP":
    print("Enjoy the show for free!")

else :
    tickets=int(input("how many tockets do you need : "))
    total=tickets*15.50
    print(f"the total cost is {total}")
    print("Enjoy your tickets!")