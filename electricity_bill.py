
n = float(input("Enter Unit Consumed: "))

total = 0
surcharge = 0

if n <= 100:
    total = n * 5

elif n < 300 and n >= 101:
    total = n * 7

elif n >= 300:
    total = n * 10

if total > 2000:
    surcharge = (total * 5) / 100

print("Unit consumed:", n)
print("Bill:", total)
print("Surcharge charges:", surcharge)
print("Total Bill:", total + surcharge)
