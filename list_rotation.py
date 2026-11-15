lst = list(map(int, input("Enter list elements separated by space: ").split()))

k = int(input("Enter number of positions to rotate: "))

direction = input("Enter direction (left/right): ").lower()

k = k % len(lst)

if direction == "left":
    lst = lst[k:] + lst[:k]

elif direction == "right":
    lst = lst[-k:] + lst[:-k]

else:
    print("Invalid direction")

print("Rotated list:", lst)
