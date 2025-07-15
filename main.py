from calculator import calculate_monthly_payment




def main():
    print("Welcome to RepayRite!")
    
    
    principal = float(input("Enter the loan amount (Principal): £"))
    rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the loan term in years: "))

    monthly_payment = calculate_monthly_payment(principal, rate, years)
    
    print(f"\nYour monthly payment is: £{monthly_payment:.2f}")

if __name__ == "__main__":
    main()