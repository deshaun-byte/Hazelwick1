tm=int(input("enter a mark from 0 to 100:"))
if tm >= 90:
    print("you got an a")
elif tm >= 80 and tm <= 89:
    print("you got a b")
elif tm >= 70 and tm <= 79:
    print("you got a c")
elif tm >= 60 and tm <= 69:
    print("you got a d")
else:
    print("you got an f")