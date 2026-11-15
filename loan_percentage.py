salary = float(input("Enter your salary: "))
age = float(input("Enter your age: "))
creditscore = float(input("Enter your credit score: "))

percentage = 0

if age >= 21 and age <= 60:
    percentage = percentage + 60

if salary >= 30000:
    percentage = percentage + 20

if creditscore >= 700:
    percentage = percentage + 20

if percentage == 80:
    print("Loan Partially Accepted")

elif percentage < 80:
    print("Loan Rejected")

else:
    print("Loan Accepted")
