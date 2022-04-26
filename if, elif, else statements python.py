#if...elif...else statements

age = int(input("Enter your age:"))
if age < 100:
    print("In", 100 - age, "years you will be 100 years old")
elif age == 100:
    print("You are", age, "years old")
else:
    print("A century and going strong!")



grade = input("Enter your grade:")

grade = int(grade)

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

print(3>=3)

age = input("How old are you?")
print(type(age))
