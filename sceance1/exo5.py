i=0
do{
nb1=int(input("devinez le chiffre"))
if nb1<nb :
   print("non c'est superieure retry")
   i++
else :
   print("non c'est inferieur retry")
   i++
}while (nb != nb1)
