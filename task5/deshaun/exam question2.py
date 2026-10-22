hours=-1
total=0
while hours<=0:
    hours=int(input("enter your amount of hours "))
    ch=input("is your car electric?")
    if ch =="yes":
        total= hours*2
        print("total cost is ",total)
    elif ch =="no":
        total= hours*4
        print("total cost is ",total)