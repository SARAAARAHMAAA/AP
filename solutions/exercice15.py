#on peut aussi utiliser la fonction in directement dans les if
def exist(text, char):
    return char.lower() in text.lower()


text=input("please enter a text : ")
if exist(text,'a'):
    print("a found")
else :
    print("a not found")

if exist(text,'e'):
    print("e found")
else :
    print("e not found")

if exist(text,'o'):
    print("o found")
else :
    print("o not found")

if exist(text,'u'):
    print("u found")
else :
    print("u not found")

if exist(text,'i'):
    print("i found")
else :
    print("i not found")

if exist(text,'y'):
    print("y found")
else :
    print("y not found")