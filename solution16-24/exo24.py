def anagrams(str1, str2):
    list1=str1.lower()
    list2=str2.lower()
    return sorted(list1) == sorted(list2)

word1 = input("Enter the first word: ").strip()
word2 = input("Enter the second word: ").strip()

if anagrams(word1, word2):
    print(f'"{word1}" and "{word2}" are anagrams!')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')
