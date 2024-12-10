text = input("please enter a string : ")

largeur = 30

espace = (largeur - len(text)) // 2 -1

ligne_horizontale = '*' * largeur

print(ligne_horizontale)
print('*' + ' ' * espace + text + ' ' * espace + '*')
print(ligne_horizontale)
