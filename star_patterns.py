
n = int(input("Enter number of rows: "))

# 1. Right Triangle
print("\nRight Triangle:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 2. Pyramid
print("\nPyramid:")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

# 3. Diamond
print("\nDiamond:")

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
