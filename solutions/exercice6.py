import math 

price=float(input("please type in a price : "))
entier= int(price)
decimal=round((price -entier)*100)
print(f"dinars : {entier}")
print(f"centimes : {decimal}")