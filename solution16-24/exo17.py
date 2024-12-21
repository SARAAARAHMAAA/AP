numbers = []
shoe_sizes = []
#methode 1
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

#methode 2
for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)
  
numbers.append(3) 
numbers.sort()
print("Numbers List:", numbers)
numbers = list(set(numbers)) 
numbers.sort()  

combined_list = numbers + shoe_sizes
print("Updated Numbers List (duplicates removed):", numbers)
print("Combined List:", combined_list)
