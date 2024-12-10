word = input("Please enter a word : ")

is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False  
        break  

if is_palindrome:
    print(f"the word : '{word}' is a palindrom.")
else:
    print(f"the word '{word}' is not a palindrom.")

