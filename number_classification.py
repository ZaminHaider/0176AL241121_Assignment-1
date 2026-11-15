
n = int(input("Enter a number: "))

if n >= 1:
    print("Number is Positive")

elif n < 0:
    print("Number is Negative")

elif n == 0:
    print("Number is zero")


if n % 2 == 0:
    print("Number is even")

else:
    print("Number is odd")


if n % 3 == 0 and n % 5 == 0:
    print("Number is divisible by 3 and 5")

else:
    print("Number is not divisible by 3 and 5")
