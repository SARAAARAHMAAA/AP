def unique_word_counter_bonus():
    print("Welcome to the Enhanced Unique Word Counter!")
    unique_words = set()
    total_words = 0

    while True:
        word = input("Enter a word: ").strip().lower()
        total_words += 1
        if word in unique_words:
            print(f"You typed in {len(unique_words)} unique words.")
            print(f"Total words entered: {total_words}")
            print("Unique words (sorted):", sorted(unique_words))

            # Sauvegarder les mots uniques dans un fichier
            with open("unique_words.txt", "w") as file:
                file.write("\n".join(sorted(unique_words)))
            print("Unique words saved to 'unique_words.txt'.")
            break
        unique_words.add(word)

# Exécution
unique_word_counter_bonus()
