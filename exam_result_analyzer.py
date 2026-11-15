a, b, c, d, e = map(float, input("Enter 5 subjects marks: ").split())

total = a + b + c + d + e
percentage = (total / 500) * 100

if a < 33 or b < 33 or c < 33 or d < 33 or e < 33:
    print("Fail")

elif percentage >= 60:
    print("First")

elif percentage >= 50:
    print("Second")

elif percentage >= 40:
    print("Third")
