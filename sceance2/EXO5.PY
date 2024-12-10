equipe1=input("entrer le nom de la premiere equipe: ")
equipe2=input("enter le nom de la deuxieme equipe: ")
resultat1=int(input(f"entrer le score de {equipe1}: "))
resultat2=int(input(f"entrer le score de {equipe2}: "))

if resultat1>resultat2:
  print(f"{equipe1} wins the game")
elif resultat2>resultat1 :
  print(f"{equipe2} wins the game")
else :
  print("it was a tie !")