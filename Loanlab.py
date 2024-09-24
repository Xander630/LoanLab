                            # Problem Analysis
#Ask User for A name and Salary
#If Salary is equal or greater than 30000 Display Eligible For loan else Display uneligible for Loan
#If Eligible Ask for a Loan amount and declare a variable for the 10x of the salary to check if eligible
#If the Loan is less than the 10x of the Salary proceed and display the interest rate
#If the Loan is greater than the 10 of the Salary Display The loan has been denied
# If the loan is less than the 10x of the Salary ask the user on Over how many months does the user plan to repay the loan
#Calculate the amount that the user has to pay use Simple Interest Formula (Principle*Rate) and add to the original loan
# Display the Final amount that the user has to pay
# End the Program


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
        Formula = loan*Interest
        result = loan + Formula
        print(f"Your Loan of ₱{loan:.2f} is approved with 10% interest ")
        print(f"Your Total Amount you have to pay in {months} month/s is ₱{result:.2f}")
        print("\n Thank you For using Xander's Bank")
    else:
        print(f"Sorry {Name}, The Loan exceeds the 10 times of your salary You're Uneligible for Loan")
        print("\n Thank you For using Xander's Bank")


else:
    print(f"Sorry {Name}, Your Salary is Too Low You're Uneligible For a Loan ")
    print("\n Thank you For using Xander's Bank")

