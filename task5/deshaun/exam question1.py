h=float(input("enter your height in cm"))
c=0
while c<=8:
    if h< 140 and h >= 120:
        ans=input("are you riding with an adult>?")
        if ans=="yes":
            print("you can ride")
            c=c+1
            if h>140:
                print("you can ride")
                c=c+1