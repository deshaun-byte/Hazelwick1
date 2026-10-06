fle=int(input("enter your first length:"))
sle=int(input("enter your second length:"))
tle=int(input("enter your third length:"))
if fle==sle and sle==tle:
    print("the triangle is equilateral")
elif fle==sle or sle==tle or tle==fle:
    print("the triangle is isosceles")
else:
    print("the triangle is scalene")