age = float(input("Enter your age: "))
salary = float(input("Enter your salary: "))
creditscore = float(input("Enter your credit score: "))

if age >= 21 and age <= 60 and salary >= 30000 and creditscore >= 700:
    print("Your loan is Approved")

elif age >= 21 and age <= 60 and ((salary >= 30000 and creditscore < 700) or (creditscore >= 700 and salary < 30000)):
    print("Loan partially approved")

else:
    print("Loan not approved")
