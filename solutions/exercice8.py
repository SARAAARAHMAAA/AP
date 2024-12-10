number=int(input("enter a number please : "))

if number%5==0 and number%3==0:
    print("FizzBUzz")
elif number%3==0 :
    print("Fizz")
elif number%5==0 :
    print("Buzz")
else :
    print("sadly nothing :(")