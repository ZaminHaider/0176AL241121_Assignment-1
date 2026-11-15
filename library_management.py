
library = {}

n = int(input("Enter number of books: "))

for i in range(n):
    name = input("Enter book name: ")
    quantity = int(input("Enter quantity: "))
    library[name] = quantity

print("\nLibrary Books:")
for name, quantity in library.items():
    print(name, ":", quantity)

book = input("\nEnter book name to search: ")

if book in library:
    print("Book available")
    print("Quantity:", library[book])
else:
    print("Book not available")

