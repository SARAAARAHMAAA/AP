while True:
    try:
        n = int(input("Please enter a positive integer: "))
        if n <= 0:
            print("The number must be positive. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

for i in range(-n, n + 1):
    if i != 0:
        print(i)
