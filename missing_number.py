lst = list(map(int, input("Enter list elements: ").split()))

n = int(input("Enter the value of n: "))

total = n * (n + 1) // 2

sum_lst = 0

for i in lst:
    sum_lst = sum_lst + i

missing = total - sum_lst

print("Missing number:", missing)
