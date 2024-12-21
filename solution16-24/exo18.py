# Initialisation de la liste
numbers = [1, 2, 3, 4, 5]

def afficher_menu():
    """Affiche le menu des opérations disponibles."""
    print("\nMenu:")
    print("1. Append (Ajouter à la fin)")
    print("2. Insert (Insérer à un index)")
    print("3. Pop (Retirer le dernier élément ou un index spécifique)")
    print("4. Remove (Supprimer un élément par valeur)")
    print("5. Sort (Trier la liste)")
    print("6. Reverse (Inverser la liste)")
    print("7. Quit (Quitter)")


while True:
    print("\nListe actuelle:", numbers)
    afficher_menu()
    
    choix = input("Choisissez une option : ")
    
    if choix == "1":  # Append
        valeur = input("Entrez une valeur à ajouter : ")
        if valeur.isdigit():
            numbers.append(int(valeur))
            print("Valeur ajoutée.")
        else:
            print("Veuillez entrer un nombre valide.")
    
    elif choix == "2":  # Insert
        valeur = input("Entrez une valeur à insérer : ")
        index = input("Entrez l'index où insérer : ")
        if valeur.isdigit() and index.isdigit():
            index = int(index)
            if 0 <= index <= len(numbers):
                numbers.insert(index, int(valeur))
                print("Valeur insérée.")
            else:
                print("Index hors limites.")
        else:
            print("Veuillez entrer des nombres valides.")
    
    elif choix == "3":  # Pop
        index = input("Entrez l'index à retirer (ou laissez vide pour le dernier élément) : ")
        if index.strip() == "":
            if numbers:  # Vérifie si la liste n'est pas vide
                numbers.pop()
                print("Dernier élément retiré.")
            else:
                print("La liste est vide.")
        elif index.isdigit():
            index = int(index)
            if 0 <= index < len(numbers):
                numbers.pop(index)
                print(f"Élément à l'index {index} retiré.")
            else:
                print("Index hors limites.")
        else:
            print("Veuillez entrer un index valide.")
    
    elif choix == "4":  # Remove
        valeur = input("Entrez la valeur à supprimer : ")
        if valeur.isdigit():
            valeur = int(valeur)
            if valeur in numbers:
                numbers.remove(valeur)
                print("Valeur supprimée.")
            else:
                print("Valeur non trouvée dans la liste.")
        else:
            print("Veuillez entrer une valeur valide.")
    
    elif choix == "5":  # Sort
        numbers.sort()
        print("Liste triée.")
    
    elif choix == "6":  # Reverse
        numbers.reverse()
        print("Liste inversée.")
    
    elif choix == "7":  # Quit
        print("Merci d'avoir utilisé le programme. Au revoir !")
        break
    
    else:
        print("Option invalide. Veuillez choisir une option valide.")
