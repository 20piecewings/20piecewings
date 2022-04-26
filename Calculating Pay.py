
hrs = input("Enter Hours:")
rph = input("Enter Rate Per Hour:")

h = float(hrs)
r = float(rph)

if h > 40:
    pay = (40 * r) + ((h - 40) * (r * 1.5))
else:
    pay = h * r
   
print(pay)




def computepay(h, r):
    return p
hrs = input("Enter Hours:")
rph = input("Enter Rate Per Hour:")
h = float(hrs)
r = float(rph)

if h > 40:
    p = (40 * r) + ((h - 40) * (r * 1.5))
else:
    p = h * r

p = computepay(h, r)
print("Pay", p)
