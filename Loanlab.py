Name = input("What is your Name: ")
Salary = float(input("What is your Current Monthly Salary?: "))

if Salary >= 30000:
    print(f"Congratulations {Name}, You are Eligible for a Loan")
    loan = float(input("How much loan would you like to borrow? : "))
    salary10x = Salary * 10 
    if loan <= salary10x:
        print("Our Bank has a Monthly Interest of 10%")
        months = int(input("How many months are you planning to pay the loan? : "))
        Interest = 0.10
        Formula = loan*Interest*months
        result = loan + Formula
        print(f"Your Loan of ₱{loan:.2f} is approved with 10% interest rate per month ")
        print(f"Your Total Amount you have to pay in {months} months is ₱{result:.2f}")
        print("\n Thank you For using Xander's Bank")
    else:
        print(f"Sorry {Name}, The Loan has been denied it exceeds the 10 times of your monthly salary")


else:
    print(f"Sorry {Name}, Your Salary is Too Low You're Uneligible For a Loan ")

