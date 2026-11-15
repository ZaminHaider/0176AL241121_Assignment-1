a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

lcm = 1

for i in range(1, (a * b) + 1):
    if i % a == 0 and i % b == 0:
        lcm = i
        break

print("HCF =", hcf)
print("LCM =", lcm)
