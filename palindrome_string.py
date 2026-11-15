s = input("Enter a string: ")

s = s.replace(" ", "").lower()

rev = s[::-1]

if s == rev:
    print("Palindrome String")
else:
    print("Not a Palindrome String")
