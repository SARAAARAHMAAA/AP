import os
def main():
    user_list = []
    while True:
        user_input = input("Entrez un nombre (ou 0 pour arrêter) : ")

        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()): #nombre positive et negative
            number = int(user_input)
        else:
            print("Veuillez entrer un nombre entier valide.")
            continue

        if number == 0:
            break

        user_list.append(number)
        print(f"Liste actuelle : {user_list}")
        print(f"Liste triée : {sorted(user_list)}")

    #Tri en ordre décroissant
    sort_order = input("Souhaitez-vous trier la liste en ordre décroissant ? (oui/non) : ").strip().lower()
    if sort_order == "oui":
        print(f"Liste triée (décroissant) : {sorted(user_list, reverse=True)}")
    
    # Calcul de la moyenne et de la médiane
    if user_list: #non vide
        mean = sum(user_list) / len(user_list)
        sorted_list = sorted(user_list)
        n = len(sorted_list)
        # Calcul de la médiane
        if n % 2 == 1:
            median = sorted_list[n // 2]
        else:
            median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        print(f"Moyenne : {mean}")
        print(f"Médiane : {median}")

    #Sauvegarder la liste dans un fichier
    save_option = input("Souhaitez-vous sauvegarder la liste dans un fichier ? (oui/non) : ").strip().lower()
    if save_option == "oui":
        filename = input("Entrez le nom du fichier pour sauvegarder la liste : ")
        with open(filename, "w") as file:
            file.write(str(user_list))
        print(f"Liste sauvegardée dans {filename}")

    #Charger et ajouter une liste existante depuis un fichier 
    #sir im not sure of the validity of this part, this is my try with functions ive found on W3Schools 
    load_option = input("Souhaitez-vous charger une liste existante depuis un fichier ? (oui/non) : ").strip().lower()
    if load_option == "oui":
        filename = input("Entrez le nom du fichier pour charger la liste : ")
        
        # Vérification de l'existence du fichier
        if os.path.exists(filename):
            with open(filename, "r") as file:
                saved_list = eval(file.read())  # Utilisation de eval pour convertir la chaîne en liste
                if isinstance(saved_list, list):  # Vérifier si le contenu du fichier est bien une liste
                    user_list = saved_list  # Remplacer la liste existante par celle chargée
                    print(f"Liste chargée et mise à jour : {user_list}")
                else:
                    print("Le fichier ne contient pas une liste valide.")
        else:
            print(f"Le fichier '{filename}' n'a pas été trouvé.")

if __name__ == "__main__":
    main()
