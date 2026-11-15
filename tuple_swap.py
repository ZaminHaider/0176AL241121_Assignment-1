
t = (10, 20, 30, 40, 50)

print("Original tuple:", t)

a, *b, c = t

t = (c, *b, a)

print("Tuple after swapping:", t)
