a = 0
b = 0
c = 0
total = 0
vote = ""
while vote != "end":
    vote = input("Enter vote (A, B, C or end): ")
    if vote == "A":
        a += 1
        total += 1
    elif vote == "B":
        b += 1
        total += 1
    elif vote == "C":
        c += 1
        total += 1
print("A:", a)
print("B:", b)
print("C:", c)
print("Total:", total)
