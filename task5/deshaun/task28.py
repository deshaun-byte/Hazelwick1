temp=int(input("Enter the temperature in Celsius: "))
if temp<0:
    print("It's freezing!")
elif temp<20:
    print("It's cold.")
elif temp<30:
    print("It's warm.")
elif temp>30:
    print("It's hot.")