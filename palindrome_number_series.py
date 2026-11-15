limit = int(input("Enter the limit: "))

for i in range(0, limit + 1):
    n = i
    rev = 0

    while n > 0:
        r = n % 10
        n = n // 10
        rev = rev * 10 + r

    if i == rev:
        print(i, end=" ")
