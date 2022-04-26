score = input("Enter Score: ")
sg = float(score)

if sg >= 90:
    print("A")
elif sg >= 80:
    print("B")
elif sg >= 70:
    print("C")
elif sg >= 60:
    print("D")
elif sg < 60:
    print("F")
else:
    print("Invalid Score")
    
    print(score)

