cities = []

while True:
    city = input("Entrez le nom d'une ville (ou 'stop' pour terminer) : ")
    
    if city == 'stop':
        break
    
    population = len(city) * 1000000
    
    cities.append([city, population])

for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        if cities[i][1] < cities[j][1]:  
            cities[i], cities[j] = cities[j], cities[i]

print("\nVilles et leurs populations (triées par population) :")
for city in cities:
    print(f"{city[0]} : {city[1]}")
